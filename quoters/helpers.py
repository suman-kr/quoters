from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen


def open_url_and_parse(_URL: str, _parser: str):
    req = Request(_URL, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    soup = bs(html, _parser)
    return soup
