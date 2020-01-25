#!/usr/bin/env python3

from quoters.extract_data import check_connection_and_generate_quote

class Quote:
    def print():
        result = check_connection_and_generate_quote()
        if result != False:
            return result
        

