from random import choice
from quoters.check_connection import is_connected
from quoters.constants import URL, SERIES_QUOTES_URL, ANIME_QUOTES_URL
import sys
import re
from quoters.enum import QuoteType
from quoters.utils import parse_with_soup


def generate_random_quote():
    soup = parse_with_soup(URL)
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
    soup = parse_with_soup(SERIES_QUOTES_URL)
    paragraphs = soup.find_all('p')
    quotes = [re.sub(r"^\d{1,}\.", "", paragraphs[i].text)
              for i in range(5, len(paragraphs) - 1)]
    return choice(quotes)


def random_anime_quote():
    soup = parse_with_soup(ANIME_QUOTES_URL)
    ul_tag = soup.find_all('ul')[3]
    quotes = []
    for tag in ul_tag.find_all('li'):
        text = re.sub(r"eval\(ez_write_tag.*\)\);", " ",
                      tag.text).replace(u'\xa0', u' ').strip()
        if len(text) != 0:
            quotes.append(text)
    return choice(quotes)
