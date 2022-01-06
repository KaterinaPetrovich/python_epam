import concurrent.futures
import json

import requests
from bs4 import BeautifulSoup, SoupStrainer


def get_info_from_the_main_page():
    base_url = "https://markets.businessinsider.com"
    main_url = "https://markets.businessinsider.com/index/components/s&p_500"
    urls = [main_url + "?p=" + str(n) for n in range(1, 12)]
    company_link = []
    companies = {}

    for url in urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        body = soup.find("tbody", class_="table__tbody")

        for row in body.find_all("tr"):
            company = row.find("td", class_="table__td table__td--big").a.text
            link = (
                base_url + row.find("td", class_="table__td table__td--big").a["href"]
            )
            company_link.append([company, link])
            change = row.find_all("span")[-1].text
            companies[company] = {"name": company, "link": link, "change": change}

    return companies, company_link


def get_info_from_the_company_page(companies, company_link):
    usd_rate = get_current_usd_rate()

    with concurrent.futures.ThreadPoolExecutor(max_workers=60) as executor:
        companies_soup = executor.map(get_soup, company_link)

    for company_soup in companies_soup:
        company = company_soup[0]
        soup = company_soup[1]
        code = soup.find("span", class_="price-section__category").span.text.strip(
            " , ,"
        )
        price = soup.find("span", class_="price-section__current-value").text.replace(
            ",", ""
        )
        price = round(float(price) * usd_rate, 2)
        pe_ratio = get_pe_ratio(soup)
        potential_profit = get_potential_profit(soup)
        companies[company].update(
            {
                "code": code,
                "price": price,
                "pe_ratio": pe_ratio,
                "potential_profit": potential_profit,
            }
        )

    return companies


def get_soup(list_link):
    page = requests.get(list_link[1])
    product = SoupStrainer("div", {"class": "graviton"})
    list_link[1] = BeautifulSoup(page.text, "html.parser", parse_only=product)
    return list_link


def get_pe_ratio(page_soup):
    pe_piece = page_soup.find_all("div", class_="snapshot__data-item")[-5]
    if "P/E Ratio" in pe_piece.text:
        pe_ratio = float(pe_piece.contents[0].strip().replace(",", ""))
    else:
        pe_ratio = float("inf")
    return pe_ratio


def get_potential_profit(page_soup):
    week_low_piece = page_soup.find_all(
        "div", class_="snapshot__data-item " "snapshot__data-item--small"
    )[-1]
    week_high_piece = page_soup.find_all(
        "div",
        class_="snapshot__data-item "
        "snapshot__data-item--small "
        "snapshot__data-item--right",
    )[-1]
    if "52 Week Low" in week_low_piece.text:
        low = float(week_low_piece.contents[0].strip().replace(",", ""))
        high = float(week_high_piece.contents[0].strip().replace(",", ""))
    else:
        return float("-inf")
    return round(((high - low) / low * 100), 2)


def get_current_usd_rate():
    cbr_url = "http://www.cbr.ru/scripts/XML_daily.asp?date_req="
    page = requests.get(cbr_url)
    soup = BeautifulSoup(page.text, "lxml")
    return float(soup.find("valute", id="R01235").value.text.replace(",", "."))


def get_sorted(companies, key, number, reverse):
    companies = companies.values()
    top_10 = sorted(companies, key=lambda c: c[key], reverse=reverse)[:number]
    return top_10


def create_json_files_top(companies):
    with open("top_high_price.json", "w") as fp:
        json.dump(get_sorted(companies, "price", 10, True), fp, indent=6)
    with open("top_low_pe_ratio.json", "w") as fp:
        json.dump(get_sorted(companies, "pe_ratio", 10, False), fp, indent=6)
    with open("top_high_change.json", "w") as fp:
        json.dump(get_sorted(companies, "change", 10, True), fp, indent=6)
    with open("top_high_potential_profit.json", "w") as fp:
        json.dump(get_sorted(companies, "potential_profit", 10, True), fp, indent=6)
