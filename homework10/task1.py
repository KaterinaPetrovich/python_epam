import asyncio
import concurrent.futures
import json
import aiohttp

import requests
from bs4 import BeautifulSoup, SoupStrainer


async def fetch_response(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            return text


async def fetch_responses(urls):
    tasks = [asyncio.create_task(fetch_response(url)) for url in urls]
    await asyncio.gather(*tasks)
    return [task.result() for task in tasks]


async def get_info_from_the_main_page():
    base_url = "https://markets.businessinsider.com"
    main_url = "https://markets.businessinsider.com/index/components/s&p_500"
    urls = [main_url + "?p=" + str(n) for n in range(1, 12)]
    pages = await fetch_responses(urls)
    # company_link = []
    companies = {}

    for page in pages:
        # page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        body = soup.find("tbody", class_="table__tbody")

        for row in body.find_all("tr"):
            company = row.find("td", class_="table__td table__td--big").a.text
            link = (
                    base_url + row.find("td", class_="table__td table__td--big")
                    .a["href"]
            )
            # company_link.append([company, link])
            change = row.find_all("span")[-1].text
            companies[company] = {"name": company,
                                  "link": link,
                                  "change": change}

    return companies


def parse_main_page(page):
    base_url = "https://markets.businessinsider.com"
    soup = BeautifulSoup(page, "html.parser")
    body = soup.find("tbody", class_="table__tbody")
    comp = []
    for row in body.find_all("tr"):
        company = row.find("td", class_="table__td table__td--big").a.text
        link = (
                base_url + row.find("td", class_="table__td table__td--big")
                .a["href"]
        )

        change = row.find_all("span")[-1].text
        comp.append({"name": company,
                     "link": link,
                     "change": change})
    return comp


def parse_company_page(page):
    product = SoupStrainer("div", {"class": "graviton"})
    soup = BeautifulSoup(page, "html.parser", parse_only=product)
    code = soup.find("span", class_="price-section__category") \
        .span.text.strip(
        " , ,"
    )
    price = soup.find("span", class_="price-section__current-value") \
        .text.replace(
        ",", ""
    )

    pe_ratio = get_pe_ratio(soup)
    potential_profit = get_potential_profit(soup)
    return {
        "code": code,
        "price": price,
        "pe_ratio": pe_ratio,
        "potential_profit": potential_profit,
    }


async def fill_dict():
    main_url = "https://markets.businessinsider.com/index/components/s&p_500"
    usd_rate = get_current_usd_rate()
    urls = [main_url + "?p=" + str(n) for n in range(1, 12)]
    pages = await fetch_responses(urls)

    companies = []

    for page in pages:
        companies += parse_main_page(page)

    urls = [company["link"] for company in companies]
    pages = await fetch_responses(urls)
    for page, company in zip(pages, companies):
        company.update(parse_company_page(page))

    for comp in companies:
        comp["price"] = round(float(comp["price"]) * usd_rate, 2)

    return companies


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
    return float(soup.find("valute", id="R01235")
                 .value.text.replace(",", "."))


def get_sorted(companies, key, number, reverse):
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
        json.dump(get_sorted(companies, "potential_profit", 10, True),
                  fp, indent=6)


async def main():
    comp = await fill_dict()
    create_json_files_top(comp)


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
    loop.close()
