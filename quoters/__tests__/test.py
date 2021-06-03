import unittest
from quoters import Quote, check_connection


class QuotersTest(unittest.TestCase):

    def test_random_quote(self):
        """
            Test random quote generation
        """
        quote = Quote().print()
        self.assertTrue(type(quote) == str)

    def test_random_series_quote(self):
        """
            Test random series quote generation
        """
        quote = Quote().print_series_quote()
        self.assertTrue(type(quote) == str)

    def test_random_anime_quote(self):
        """
            Test random anime quote generation
        """
        quote = Quote().print_anime_quote()
        self.assertTrue(type(quote) == str)

    def test_internet_connectivity(self):
        """
            Test internet connectivity
        """
        connection = check_connection.is_connected()
        self.assertEqual(connection, True)


if __name__ == '__main__':
    unittest.main()
