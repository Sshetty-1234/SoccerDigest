from bs4 import BeautifulSoup
import requests

url = "https://www.bbc.com/sport/football/"

response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
elements = soup.find_all("li",class_="ssrcss-rs7w2i-ListItem e1gp961v0")
counter = 0
for element in elements:
    a_tag = element.find("a")
    link = (f"https://bbc.com{a_tag['href']}")
    live_link = requests.get(link)
    live_soup = BeautifulSoup(live_link.text,"html.parser")
    check = live_soup.find("div", class_="ssrcss-uf6wea-RichTextComponentWrapper ep2nwvo0")
    check = str(type(check))
    if "bs4.element" in check:
        print(check)
        sources = live_soup.find_all("div", class_="ssrcss-uf6wea-RichTextComponentWrapper ep2nwvo0")
        print(type(sources))
        for source in sources:
            print(source.text)
            print("")
        print("-------------------------------------------------------")
    
    if counter > 5:
        break



    