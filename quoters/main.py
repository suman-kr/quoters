#!/usr/bin/env python3

from quoters.extract_data import check_connection_and_generate_quote
from quoters.enum import QuoteType

class Quote:
    def print():
        result = check_connection_and_generate_quote(QuoteType.QUOTE)
        if result != False:
            return result
        

    def print_series_quotes():
        result = check_connection_and_generate_quote(QuoteType.SERIES_QUOTE)
        if result != False:
            return result