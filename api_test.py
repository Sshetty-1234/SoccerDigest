import requests
import json

API_KEY = '15cd8b6230734db5ba0f5f6fe511616f'
BASE_URL = 'https://api.football-data.org/v4'

headers = {
    'X-Auth-Token': API_KEY
}

def get_competitions():
    endpoint = f"{BASE_URL}/teams/61/matches?dateFrom=2024-12-01&dateTo=2024-12-02"
    
    response = requests.get(endpoint, headers=headers)
    
    # Check for successful response
    if response.status_code == 200:
        data = response.json()
        homeTeam = data["matches"][0]["homeTeam"]['name']
        for i in range(4):    
            try:
                homeTeam = data["matches"][i]["homeTeam"]['name']
                print(homeTeam)
            except IndexError as e:
                print("cannot access")
        # homeTeam = data["matches"][0]["homeTeam"]['name']
        # awayTeam = data["matches"][0]["awayTeam"]['name']
        # league = data["matches"][0]["competition"]['name']
        # matchDay = data["matches"][0]["season"]['currentMatchday']
        # date = data["matches"][0]["utcDate"][:10]
        # time = data["matches"][0]["utcDate"][11:19]
        # print(time)
        # pretty_json = json.dumps(data, indent=4)
        # print(pretty_json)
    else:
        print(f"Error: {response.status_code}, {response.text}")

# Call the function
get_competitions()
