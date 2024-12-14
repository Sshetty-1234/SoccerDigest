import requests
from bs4 import BeautifulSoup


url = 'https://www.premierleague.com/tables'
page = requests.get(url)

soup = BeautifulSoup(page.text,"html.parser")

table = soup.find("tbody")
ranks = []
count = 1
for i in range(1,21):

    team = table.find("tr", {"data-position":i})

    team_name = team.find("a").find("span",class_="league-table__team-name league-table__team-name--long long")
    #pos = team.find("td").find("span",class_="league-table__result-highlight").text.strip()
    pos = count
    team_info = team.find_all("td")[2:10]
    team_standing = {
            "Club" : team_name.text,
            "Rank" : pos,
            "Played" : team_info[0].text,
            "Wins" : team_info[1].text,
            "Draws" : team_info[2].text,
            "Losses" : team_info[3].text,
            "Goal_difference" : team_info[6].text.strip(),
            "Points" :team_info[7].text
    }

    ranks.append(team_standing)
    team_standing = {}
    count += 1

