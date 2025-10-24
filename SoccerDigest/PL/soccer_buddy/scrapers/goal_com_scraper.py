import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Referer': 'https://www.google.com/'
}

url = 'https://www.goal.com/en-us'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

breaking_news_div = soup.find('div', class_="breaking-news_breaking-news__zVGt9 component-breaking-news")
articles = breaking_news_div.find_all('article', class_="card_card__iEGd_") if breaking_news_div else []

article_content = ""
for counter, article in enumerate(articles[:5], 1):
    a_tag = article.find('a', href=True)
    if a_tag:
        link = "https://goal.com" + a_tag['href']
        news_response = requests.get(link, headers=headers)
        news_soup = BeautifulSoup(news_response.text, 'html.parser')
        text_summary = news_soup.find("div", class_="article_content__4siWz")
        article_content += f"\n--- ARTICLE {counter} CONTENT ---\n"
        if text_summary:
            article_content += text_summary.get_text(strip=True)
        else:
            article_content += "Could not find content summary for this article."
        article_content += "\n--------------------------------\n"


