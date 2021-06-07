#!/usr/bin/env python3

from quoters.extract_data import check_connection_and_generate_quote
from quoters.enum import QuoteType


class Quote:
    """
        Class Quote to print random `quotes` and `TV series quotes`
    """
    @staticmethod
    def print(offline=False):
        """
            Function to return random quotes
            Parameters
            ----------
            offline: Boolean, optional
                To support offline usage (default is False)
        """
        result = check_connection_and_generate_quote(QuoteType.QUOTE, offline)
        if result != False:
            return result

    @staticmethod
    def print_series_quote(offline=False):
        """
            Function to return random TV shows quotes
            Parameters
            ----------
            offline: Boolean, optional
                To support offline usage (default is False)
        """
        result = check_connection_and_generate_quote(
            QuoteType.SERIES_QUOTE, offline)
        if result != False:
            return result

    @staticmethod
    def print_anime_quote(offline=False):
        """
            Function to return random anime quotes
            Parameters
            ----------
            offline: Boolean, optional
                To support offline usage (default is False)
        """
        result = check_connection_and_generate_quote(
            QuoteType.ANIME_QUOTE, offline)
        if result != False:
            return result

    @staticmethod
    def print_programming_quote(offline=False):
        """
            Function to return random programming quotes
            Parameters
            ----------
            offline: Boolean, optional
                To support offline usage (default is False)
        """
        result = check_connection_and_generate_quote(
            QuoteType.PROGRAMMING_QUOTE, offline)
        if result != False:
            return result
