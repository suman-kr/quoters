#! /usr/bin/env python3

import sys
from quoters import extract_data
from quoters.enum import QuoteType


def main():
    try:
        print(extract_data._fetch_offline_quotes(QuoteType.QUOTE))
        return 0
    except:
        return 1


if __name__ == "__main__":
    sys.exit(main())
