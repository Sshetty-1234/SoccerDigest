from django.shortcuts import render, HttpResponse,get_object_or_404
from .models import Team,soccer_buddy,club_info
import requests
from .soccer_buddy.summarize import run
from datetime import date,timedelta
import json
import os
from dotenv import load_dotenv
load_dotenv()
today = date.today()
future_date = today + timedelta(days=14)

try:
    PRE_COMPUTED_CONTENT = run()
except Exception as e:
    PRE_COMPUTED_CONTENT = f"Summary is currently unavailable: {e}"

############################## VIEWS ##############################
headers = {
    'X-Auth-Token': os.getenv('FOOTBALL_API')
    }
endpoint = f"https://api.football-data.org/v4/competitions/PL/standings"
response = requests.get(endpoint, headers=headers)
data = json.loads(response.text)
table = data['standings'][0]['table']
# Create a clean list of dictionaries
ranks = []
for team in table:
    team_info = {
    "club": team['team']['name'],
    "rank": team['position'],
    "played": team['playedGames'],
    "wins": team['won'],
    "draws": team['draw'],
    "losses": team['lost'],
    "goal_difference": team['goalDifference'],
    "points": team['points'],
    "gf": team['goalsFor'],
    "ga": team['goalsAgainst'],
}
    ranks.append(team_info)
        
# Create your views here.
def home(request):
    return HttpResponse('invalid page')

def team_info(request,name):
    desired_club = Team.objects.filter(team = name)
    club_stuff = club_info.objects.filter(club_name = name)
    id = club_stuff[0].club_id
    matches = match_info(id)
    return render(request, "club_data.html", {"club": desired_club,"matches":matches,"info":club_stuff})

def soccer(request):
    all_clubs = Team.objects.all().values_list('team', flat=True).distinct()
    icon = soccer_buddy.objects.first()
    return render(request,"team.html",{"clubs":all_clubs,"soccer_buddy":icon,'news_info':PRE_COMPUTED_CONTENT})

def rankings(request):
    
    return render(request,"rankings.html",{"standing":ranks})


def match_info(id: int):
    # header = {
    # 'X-Auth-Token': os.getenv("FOOTBALL_DATA_API_KEY")
    # }
    header ={
        'X-Auth-Token': os.getenv('FOOTBALL_API')
    }
    # idk why but i had to delete the restart the api key account
    # for the api to work again. not sure if it was account ran out of credits
    # to fix it simply just made a new account
    # and checked with api_test.py
    BASE_URL = "https://api.football-data.org/v4/"
    response = requests.get(f"{BASE_URL}teams/{id}/matches?dateFrom={today}&dateTo={future_date}", headers=header)
    data = response.json()
    games = []
    if response.status_code == 200:
        for i in range(2):# because I only want the top 2 games
            try:
                homeTeam = data["matches"][i]["homeTeam"]['name']
                awayTeam = data["matches"][i]["awayTeam"]['name']
                league = data["matches"][i]["competition"]['name']
                matchDay = data["matches"][i]["season"]['currentMatchday']
                date = data["matches"][i]["utcDate"][:10]
                time = data["matches"][i]["utcDate"][11:19]
                match = {
                    "homeTeam" : homeTeam,
                    "awayTeam" : awayTeam,
                    "league" : league,
                    "matchDay" : matchDay,
                    "date" : date,
                    "time":time
                }
                games.append(match)
                match = {}
            except IndexError as e:
                break
    return games

