from collections import Counter

import requests


def count_dots_on_i(url: str) -> int:
    try:
        html_string = requests.get(url).text
    except requests.exceptions.RequestException:
        raise ValueError()
    return Counter(html_string).get("i")
