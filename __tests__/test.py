import unittest
from quoters import main as quoters
from quoters import check_connection


class QuotersTest(unittest.TestCase):

    def test_random_quote(self):
        """
            Test random quote generation
        """
        quote = quoters.Quote().print()
        self.assertTrue(type(quote) == str)

    def test_random_series_quote(self):
        """
            Test random series quote generation
        """
        quote = quoters.Quote().print_series_quote()
        self.assertTrue(type(quote) == str)

    def test_random_anime_quote(self):
        """
            Test random anime quote generation
        """
        quote = quoters.Quote().print_anime_quote()
        self.assertTrue(type(quote) == str)

    def test_internet_connectivity(self):
        """
            Test internet connectivity
        """
        connection = check_connection.is_connected()
        self.assertEqual(connection, True)


if __name__ == '__main__':
    unittest.main()
