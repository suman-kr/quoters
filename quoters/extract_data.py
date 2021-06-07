from random import choice, randint
from quoters.check_connection import is_connected
from quoters.constants import *
import sys
import re
from quoters.enum import QuoteType
from quoters.wrapper import Wrapper
from quoters.helpers import open_url_and_parse


def generate_random_quote():
    soup = open_url_and_parse(URL, "html.parser")
    quotes = [i.text.strip().replace("\n", " ")
              for i in soup.find_all('blockquote')]
    return choice(quotes)


def _fetch_offline_quotes(_type: QuoteType):
    if _type == QuoteType.QUOTE:
        return Wrapper("quote.json").find_quote(str(randint(0, 96)))
    if _type == QuoteType.SERIES_QUOTE:
        return Wrapper("series.json").find_quote(str(randint(0, 49)))
    if _type == QuoteType.ANIME_QUOTE:
        return Wrapper("anime.json").find_quote(str(randint(0, 103)))
    if _type == QuoteType.PROGRAMMING_QUOTE:
        return Wrapper("programming.json").find_quote(str(randint(0, 99)))


def check_connection_and_generate_quote(_type: QuoteType, offline=False):
    try:
        if is_connected():
            if _type == QuoteType.QUOTE:
                return generate_random_quote()
            if _type == QuoteType.SERIES_QUOTE:
                return random_series_quote()
            if _type == QuoteType.ANIME_QUOTE:
                return random_anime_quote()
            if _type == QuoteType.PROGRAMMING_QUOTE:
                return random_programming_quote()
        else:
            if offline:
                return _fetch_offline_quotes(_type)
            print("Site not reachable!\nPlease check your connection")
            return False
    except:
        raise OSError


def random_series_quote():
    soup = open_url_and_parse(SERIES_QUOTES_URL, "html.parser")
    paragraphs = soup.find_all('p')
    quotes = [re.sub(r"^\d{1,}\.", "", paragraphs[i].text)
              for i in range(5, len(paragraphs) - 1)]
    return choice(quotes)


def random_anime_quote():
    soup = open_url_and_parse(ANIME_QUOTES_URL, "html5lib")
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


def random_programming_quote():
    soup = open_url_and_parse(PROGRAMMING_QUOTES_URL, "html5lib")
    ol_tags = soup.find_all("ol")
    quotes = [list_tag.text.replace("(source)", "").strip()
              for lists in ol_tags for list_tag in lists]
    return choice(quotes)
