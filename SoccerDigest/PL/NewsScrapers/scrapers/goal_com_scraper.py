import requests
from bs4 import BeautifulSoup




headers = {
    'Referer': 'https://www.google.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://goal.com/en-us', headers=headers)

soup = BeautifulSoup(response.text, "html.parser")



articles = soup.find_all('li', class_="item card-list-item_bg-for-shadow__7rgUQ")

counter = 1
article_content = ""

for article in articles:
    a_tag = article.find('a', href=True)  # Find the 'a' tag with an 'href' attribute
    if a_tag and "lists" in a_tag['href']:
        link = "https://goal.com" + a_tag['href']
        print(f"Article {counter}")
        print(link)
        news_article = requests.get(link)
        news_soup = BeautifulSoup(news_article.text,"html.parser")
        text_summary = news_soup.find("div", class_="article_content__4siWz")
        article_content = article_content + text_summary.text
        
        counter = counter + 1
        
        # Gives the summary of the top 5 articles
        if counter > 5:
            break
        
        
