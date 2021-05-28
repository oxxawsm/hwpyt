import re
import typing as tp

import requests
from bs4 import BeautifulSoup


def extract_news(parser: BeautifulSoup) -> tp.List[tp.Dict[str, tp.Any]]:
    """ Extract news from a given web page """

    news_list = []

    authors = [i.text for i in parser.body.find_all("a", {"class": "hnuser"})]
    comments = [
        i for i in parser.body.find_all("a") if "item?id=" in i.attrs["href"]
    ]  # link
    comments = [
        i.text for i in comments if (re.match(r"\d+\scomment", i.text) or i.text == "discuss")
    ]  # text
    comment_counts = [
        int(i[: i.find("\xa0")]) if not "discuss" in i else 0 for i in comments
    ]
    points = [
        int(i.text[: i.text.find(" ")]) for i in parser.body.find_all("span", {"class": "score"})
    ]
    titles = [i.text for i in parser.body.find_all("a", {"class": "storylink"})]
    urls = [
        i.attrs["href"] for i in parser.body.find_all("a", {"class": "storylink"})
    ]

    for i, _ in enumerate(authors):
        extract = {
            "author": authors[i],
            "comments": comment_counts[i],
            "points": points[i],
            "title": titles[i],
            "url": urls[i],
        }
        news_list.append(extract)

    return news_list


def extract_next_page(parser: BeautifulSoup) -> str:
    """ Extract next page URL """

    morelink: str = parser.body.find("a", {"class": "morelink"}).attrs["href"]

    return morelink


def get_news(url: str, n_pages: int = 1):
    """ Collect news from a given web page """

    news = []
    while n_pages:
        print("Collecting data from page: {}".format(url))
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        news_list = extract_news(soup)
        next_page = extract_next_page(soup)
        url = "https://news.ycombinator.com/" + next_page
        news.extend(news_list)
        n_pages -= 1

    return news
