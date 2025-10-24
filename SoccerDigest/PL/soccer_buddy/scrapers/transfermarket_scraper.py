import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Referer': 'https://www.google.com/'
}

url = 'https://www.marca.com/en/football/transfer-market.html'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('div', class_='ue-c-cover-content__body')  # Each transfer news block
article_content = ""
for i, article in enumerate(articles[:5], 1):
    a_tag = article.find('a', href=True)
    if a_tag:
        link = a_tag['href']
        title = a_tag.get_text(strip=True)

        news_response = requests.get(link, headers=headers)
        news_soup = BeautifulSoup(news_response.text, 'html.parser')
        content_div = news_soup.find('div', class_='ue-l-article__body')  # Main article content

        article_content += content_div.get_text(strip=True) if content_div else "Content not found"
        
        
