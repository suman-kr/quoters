
from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
from random import choice
from quoters.check_connection import is_connected
from quoters.constants import URL
import sys


def generate_random_quote():
        req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
        html = urlopen(req).read()
        soup = bs(html , 'html.parser')
        a = [i.text.strip().replace("\n", " ") for i in soup.find_all('blockquote')]
        return choice(a)

def check_connection_and_generate_quote():
    try:
        if is_connected():
            generate_random_quote()  
        else:
            print("Site not reachable!\nPlease check your connection")
    except:
        raise OSError
