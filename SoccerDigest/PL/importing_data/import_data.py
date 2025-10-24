import os
import sys
import django
import pandas as pd

# --- Setup Django environment ---
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SoccerDigest.settings')
django.setup()

# --- Import Django model ---
from PL.models import Team

# --- Utility functions ---
def safe_int(value):
    """Convert to int, keep digits only. Returns None if fails."""
    if pd.isna(value):
        return None
    try:
        return int(str(value).split('-')[0].replace(',', '').strip())
    except:
        return None

def safe_float(value):
    """Convert to float, replace comma with dot. Returns None if fails."""
    if pd.isna(value):
        return None
    try:
        return float(str(value).replace(',', '.').strip())
    except:
        return None

# --- Load CSV ---
csv_file_path = '/Users/sohamshetty/Desktop/SoccerDigest/SoccerDigest/PL/importing_data/database.csv'
df = pd.read_csv(csv_file_path)
df.columns = df.columns.str.strip()

# --- Import rows ---
for index, row in df.iterrows():
    try:
        team = Team(
            player=row.get('Player', ''),
            team=row.get('Team', ''),
            number=safe_int(row.get('#')),
            nation=row.get('Nation', None),
            position=row.get('Position', None),
            age=safe_int(row.get('Age')),
            minutes=safe_float(row.get('Minutes')),
            goals=safe_int(row.get('Goals')),
            assists=safe_int(row.get('Assists')),
            penalty_shoot_on_goal=safe_int(row.get('Penalty Shoot on Goal')),
            penalty_shoot=safe_int(row.get('Penalty Shoot')),
            total_shoot=safe_int(row.get('Total Shoot')),
            shoot_on_target=safe_int(row.get('Shoot on Target')),
            yellow_cards=safe_int(row.get('Yellow Cards')),
            red_cards=safe_int(row.get('Red Cards')),
            touches=safe_int(row.get('Touches')),
            dribbles=safe_int(row.get('Dribbles')),
            tackles=safe_int(row.get('Tackles')),
            blocks=safe_int(row.get('Blocks')),
            expected_goals_xg=safe_float(row.get('Expected Goals (xG)')),
        )
        team.save()
    except Exception as e:
        print(f"⚠️ Error saving row {index}: {e}")

print("✅ CSV data has been successfully loaded into the Django database.")
