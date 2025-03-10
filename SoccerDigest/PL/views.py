from django.shortcuts import render, HttpResponse,get_object_or_404
from .models import Team, club_info, soccer_buddy
import requests
from .rankings import ranks
from .NewsScrapers.summarize import response as ans
from datetime import date,timedelta
import os



today = date.today()
future_date = today + timedelta(days=14)



# Create your views here.

def check(request):
    return render(request,"rankings.html")

def soccer(request):
    all_clubs = Team.objects.all().values_list('club_name', flat=True).distinct()
    icon = soccer_buddy.objects.first()
    return render(request,"team.html",{"clubs":all_clubs,"soccer_buddy":icon,"news_info":ans})

def team_info(request,name):
    desired_club = Team.objects.filter(club_name = name)
    club_stuff = club_info.objects.filter(club_name = name)
    id = club_stuff[0].club_id
    matches = match_info(id)
    return render(request, "club_data.html",{"club":desired_club,"matches":matches,"info":club_stuff})
    #return render(request, "club_data.html",{"club":desired_club})

def rankings(request):
    return render(request,"rankings.html",{"standing":ranks})

def testing(request):
    club_name = Team.objects.filter(club_name = "Tottenham Hotspur")
    return render(request,"index.html",{"club":club_name})

def match_info(id: int):
    # header = {
    # 'X-Auth-Token': os.getenv("FOOTBALL_DATA_API_KEY")
    # }
    header ={
        'X-Auth-Token': '2b24fe9754c54bac8868b6f567124c5e'
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

