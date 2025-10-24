import requests
from bs4 import BeautifulSoup
import pandas as pd

urls = [
    "https://fbref.com/en/squads/e4a775cb/Nottingham-Forest-Stats",
    "https://fbref.com/en/squads/4ba7cbea/Bournemouth-Stats",
    "https://fbref.com/en/squads/47c64c55/Crystal-Palace-Stats",
    "https://fbref.com/en/squads/d3fd31cc/Everton-Stats",
    
    
]
'''

"https://fbref.com/en/squads/a2d435b3/Leicester-City-Stats",
    "https://fbref.com/en/squads/b74092de/Ipswich-Town-Stats",
    "https://fbref.com/en/squads/8cec06e1/Wolverhampton-Wanderers-Stats",
    "https://fbref.com/en/squads/33c895d4/Southampton-Stats"
    
    

"https://fbref.com/en/squads/18bb7c10/Arsenal-Stats",
    "https://fbref.com/en/squads/822bd0ba/Liverpool-Stats",
    "https://fbref.com/en/squads/b8fd03ef/Manchester-City-Stats",
    "https://fbref.com/en/squads/cff3d9bb/Chelsea-Stats",
    "https://fbref.com/en/squads/8602292d/Aston-Villa-Stats",
    "https://fbref.com/en/squads/d07537b9/Brighton-and-Hove-Albion-Stats",
    "https://fbref.com/en/squads/b2b47a98/Newcastle-United-Stats",
    "https://fbref.com/en/squads/19538871/Manchester-United-Stats",
    "https://fbref.com/en/squads/361ca564/Tottenham-Hotspur-Stats",
    "https://fbref.com/en/squads/fd962109/Fulham-Stats",
    "https://fbref.com/en/squads/cd051869/Brentford-Stats",
    "https://fbref.com/en/squads/7c21e445/West-Ham-United-Stats",
'''
all_data = []  

for url in urls:
    page = requests.get(url)
    print(url)
    print(page)

    soup = BeautifulSoup(page.text, "html.parser")

    table = soup.find("tbody")

    site_title = soup.find("h1").text
    team_name = ""

    players = table.find_all("tr")

    data = []  # Initialize an empty list for each URL's data

    # Getting the club name
    player_url = f"https://fbref.com{table.find('th').find('a')['href']}"
    player_page = requests.get(player_url)
    player_soup = BeautifulSoup(player_page.text, "html.parser")
    club_name = player_soup.find("strong", string='Club:').find_next("a").text

    for player in players:
        player_data = {}
        
        player_data["Name"] = player.find('th').text
        player_data["Nation"] = player.find('td', {'data-stat': 'nationality'}).find("a").find("span").text[3:]
        player_data["Pos"] = player.find('td',{'data-stat': 'position'}).text
        player_data["Age"] = player.find('td',{'data-stat': 'age'}).text[:2]
        player_data["MP"] = player.find('td',{'data-stat': 'games'}).text
        player_data["Games Played"] = player.find('td',{'data-stat': 'games_starts'}).text
        player_data["Gls"] = player.find('td',{'data-stat': 'goals'}).text
        player_data["Ast"] = player.find('td',{'data-stat': 'assists'}).text
        player_data["CrdY"] = player.find('td',{'data-stat': 'cards_yellow'}).text
        player_data["CrdR"] = player.find('td',{'data-stat': 'cards_red'}).text
        player_data["xG"] = player.find('td',{'data-stat': 'xg_per90'}).text
        player_data["Club"] = club_name
        
        data.append(player_data)

    all_data.extend(data)  

df = pd.DataFrame(all_data)
df.to_csv('soccer_3.csv', index=False)
print(df.head())
