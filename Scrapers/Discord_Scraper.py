import requests
import re
from bs4 import BeautifulSoup

def url_requests():

    URL = "https://eldenring.wiki.fextralife.com/Arrows+and+Bolts"
    page = requests.get(URL)
    Content = BeautifulSoup(page.content, 'html.parser')
    
    
def main():
    url_requests()

if __name__ == "__main__":
    main()