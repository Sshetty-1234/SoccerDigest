import requests
from bs4 import BeautifulSoup


url = 'https://www.espn.com/soccer/standings/_/league/eng.1'
page = requests.get(url)
print(page.status_code)
