import requests
import json

API_KEY = '2b24fe9754c54bac8868b6f567124c5e'
BASE_URL = 'https://api.football-data.org/v4'

headers = {
    'X-Auth-Token': API_KEY
}
endpoint = f"{BASE_URL}/competitions/PL/standings"
response = requests.get(endpoint, headers=headers)
data = json.loads(response.text)
table = data['standings'][0]['table']

# Create a clean list of dictionaries
ranks = []
for team in table:
    team_info = {
        "Club": team['team']['name'],
        "Rank": team['position'],
        "Played": team['playedGames'],
        "Wins": team['won'],
        "Draws": team['draw'],
        "Losses": team['lost'],
        "Goal_difference": team['goalDifference'],
        "Points": team['points'],
        "GF": team['goalsFor'],
        "GA": team['goalsAgainst'],
        
    }
    ranks.append(team_info)

# Print nicely
print(json.dumps(ranks, indent=4))

    
