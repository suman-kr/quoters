from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen

def parse_with_soup(URL: string):
    req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    soup = bs(html, 'html.parser')
    return soup