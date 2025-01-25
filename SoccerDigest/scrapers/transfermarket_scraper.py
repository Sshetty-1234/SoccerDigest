from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.marca.com/en/football/transfer-market.html")
soup = BeautifulSoup(page.text, "html.parser")

counter = 1

article_content = " "

articles = soup.find_all("div", class_="ue-l-cover-grid__unit ue-l-cover-grid__unit--no-grow")
for article in articles:
    link = article.find("a")["href"]
    print(f"Article No: {counter}")
    print(f"Article title: {article.find('h2', class_='ue-c-cover-content__headline').text}")
    print(f"link: {link}")
    
    news = requests.get(link)
    news_soup = BeautifulSoup(news.text,"html.parser")
    elements = news_soup.find("div", class_="ue-c-article__body").find_all("p")
    for element in elements:
        article_content = article_content + element.text
        
    print("\n")
    counter = counter +  1
    
    break
    



