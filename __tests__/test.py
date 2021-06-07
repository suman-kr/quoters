import unittest
from quoters import Quote, check_connection
from fastapi.testclient import TestClient
from api.main import app

api_client = TestClient(app)


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

    def test_random_quotes_api(self):
        """
            Test api response for random quotes
        """
        response = api_client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_random_anime_quotes_api(self):
        """
            Test api response for random anime quotes
        """
        response = api_client.get("/?query=anime")
        self.assertEqual(response.status_code, 200)

    def test_random_series_quotes_api(self):
        """
            Test api response for random series quotes
        """
        response = api_client.get("/?query=series")
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
