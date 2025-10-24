import requests
from bs4 import BeautifulSoup


url = "https://apnews.com/hub/soccer"
response = requests.get(url)

print(response)

soup = BeautifulSoup(response.text,"html.parser")
articles = soup.find_all("div",class_="PageList-items-item")
count = 0
article_content = " "
for article in articles:
    if(count > 4):
        link = article.find("a")["href"]
        print(link.strip())
        print("")
        
        news_link = requests.get(link)
        news_soup = BeautifulSoup(news_link.text,"html.parser")
        news_article = news_soup.find("div",class_="RichTextStoryBody RichTextBody")
        article_content = article_content + news_article.text.strip()
        print("")
        print("----------------------------------------------------------------")
        
    
    count = count + 1
    
    
    if(count > 8):
        break
