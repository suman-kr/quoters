from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
from random import choice
from quoters.check_connection import is_connected
from quoters.constants import URL, SERIES_QUOTES_URL, ANIME_QUOTES_URL
import sys
import re
from quoters.enum import QuoteType

def generate_random_quote():
    req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    soup = bs(html, 'html.parser')
    quotes = [i.text.strip().replace("\n", " ")
              for i in soup.find_all('blockquote')]
    return choice(quotes)


def check_connection_and_generate_quote(_type: QuoteType):
    try:
        if is_connected():
            if _type == QuoteType.QUOTE:
                return generate_random_quote()
            if _type == QuoteType.SERIES_QUOTE:
                return random_series_quote()
            if _type == QuoteType.ANIME_QUOTE:
                return random_anime_quote()
        else:
            print("Site not reachable!\nPlease check your connection")
            return False
    except:
        raise OSError


def random_series_quote():
    req = Request(SERIES_QUOTES_URL, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    soup = bs(html, 'html.parser')
    paragraphs = soup.find_all('p')
    quotes = [re.sub(r"^\d{1,}\.", "", paragraphs[i].text)
                        for i in range(5, len(paragraphs) - 1)]
    return choice(quotes)


def random_anime_quote():
    req = Request(ANIME_QUOTES_URL, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    soup = bs(html, 'html5lib')
    ul_tag = soup.find_all('ul')[3]
    quotes = []
    for tag in ul_tag.find_all('li'):
        text = tag.text.replace(u'\xa0', u' ').strip()
        ind = text.find("if(typeof")
        if ind > -1:
            text = text[0: ind]
        if len(text) > 0:
            quotes.append(text)
    return choice(quotes)