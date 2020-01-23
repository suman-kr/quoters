#!/usr/bin/env python3

from quoters.extract_data import check_connection_and_generate_quote

class Quote:
    def __str__(self):
        return check_connection_and_generate_quote()

