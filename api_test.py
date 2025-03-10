import requests
import json

API_KEY = '2b24fe9754c54bac8868b6f567124c5e'
BASE_URL = 'https://api.football-data.org/v4'

headers = {
    'X-Auth-Token': API_KEY
}
# id = 61
# print(requests.get(f"{BASE_URL}/teams/{id}",headers=headers).status_code)

def get_competitions():
    endpoint = f"{BASE_URL}/teams/61/matches?dateFrom=2025-03-01&dateTo=2025-05-10"
    
    response = requests.get(endpoint, headers=headers)
    
    # Check for successful response
    if response.status_code == 200:
        data = response.json()
        # homeTeam = data["matches"][0]["homeTeam"]['name']
        # for i in range(4):    
        #     try:
        #         homeTeam = data["matches"][i]["homeTeam"]['name']
        #         print(homeTeam)
        #     except IndexError as e:
        #         print("cannot access")
        homeTeam = data["matches"][1]["homeTeam"]['name']
        print(homeTeam)
        awayTeam = data["matches"][0]["awayTeam"]['name']
        league = data["matches"][0]["competition"]['name']
        matchDay = data["matches"][0]["season"]['currentMatchday']
        date = data["matches"][0]["utcDate"][:10]
        time = data["matches"][0]["utcDate"][11:19]
        #print(time)
        pretty_json = json.dumps(data, indent=4)
        #print(pretty_json)
    else:
        print(f"Error: {response.status_code}, {response.text}")

# Call the function
get_competitions()

# import requests
# import json

# uri = 'https://api.football-data.org/v4/teams/61/matches?dateFrom=2025-03-01&dateTo=2025-05-01'
# headers = { 'X-Auth-Token': '2b24fe9754c54bac8868b6f567124c5e' }

# response = requests.get(uri, headers=headers)
# print(json.dumps(response.json()['matches'][1]["homeTeam"]["name"], indent = 2))