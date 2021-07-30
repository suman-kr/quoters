#! /usr/bin/env python3

import sys
from quoters import extract_data
from quoters.enum import QuoteType

BOLD = "\033[1m"
END = "\033[0m"
UNDERLINE = "\033[4m"

help_message = f"""Minimal HELP to get you started..\n
Choose from the following categories:
- {BOLD}quote{END}: Motivating quote
- {BOLD}series{END}: TV shows quote
- {BOLD}anime{END}: Anime quote
- {BOLD}programming{END}: Programming quote

Usage Example:
 {BOLD}quoters anime{END}

{UNDERLINE}Try again!{END}
"""

switcher = {
    "anime": extract_data._fetch_offline_quotes(QuoteType.ANIME_QUOTE),
    "series": extract_data._fetch_offline_quotes(QuoteType.SERIES_QUOTE),
    "programming":
    extract_data._fetch_offline_quotes(QuoteType.PROGRAMMING_QUOTE),
    "quote": extract_data._fetch_offline_quotes(QuoteType.QUOTE),
    "help": help_message
}


def quote_category(category):
    return switcher.get(category)


def parse_arguments(arg):
    if arg not in switcher.keys():
        return "Invalid category!. Try some {}help{}.".format(BOLD, END)
    return quote_category(arg)


def main():
    try:
        if len(sys.argv) > 2:
            print(
                "Too many arguments!! It's amusing how we get this wrong. Try some {}help{}."
                .format(BOLD, END))
            return 1
        elif len(sys.argv) == 1:
            print(quote_category("quote"))
        else:
            input = parse_arguments(sys.argv[1])
            print(input)
        return 0
    except:
        return 1


if __name__ == "__main__":
    sys.exit(main())
