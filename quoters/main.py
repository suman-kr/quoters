#!/usr/bin/env python3

from quoters.extract_data import check_connection_and_generate_quote
from quoters.enum import QuoteType

class Quote:
    """
        Class Quote to print random `quotes` and `TV shows quotes`
    """
    @staticmethod
    def print():
        """
            Function to return random quotes
        """
        result = check_connection_and_generate_quote(QuoteType.QUOTE)
        if result != False:
            return result

    @staticmethod
    def print_series_quote():
        """
            Function to return random TV shows quotes
        """
        result = check_connection_and_generate_quote(QuoteType.SERIES_QUOTE)
        if result != False:
            return result

    @staticmethod
    def print_anime_quote():
        """
            Function to return random anime quotes
        """
        result = check_connection_and_generate_quote(QuoteType.ANIME_QUOTE)
        if result != False:
            return result
