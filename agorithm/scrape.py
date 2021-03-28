import requests
from bs4 import BeautifulSoup

URL = 'https://steamdb.info/'

page = requests.get(URL)
print(page.status_code)
soup = BeautifulSoup(page.content, 'html.parser')



