import pandas as pd
#from django.contrib.auth.models import User
from PL.models import Team  # Adjust this import to match your app name

# Read CSV file into a DataFrame
csv_file_path = '/Users/sohamshetty/Desktop/Projects/SoccerDigest/soccer.csv'  # Update with the correct path
df = pd.read_csv(csv_file_path)

# # Iterate through the DataFrame and create model instances
# for index, row in df.iterrows():
#     try:
#         # Create the Team instance
#         team = Team(
#             name=row['Name'],
#             nation=row['Nation'],
#             pos=row['Pos'],
#             age=int(row['Age']) if pd.notna(row['Age']) else None,
#             gp=int(row['Games Played']) if pd.notna(row['Games Played']) else None,
#             ast=int(row['Ast']) if pd.notna(row['Ast']) else None,
#             crd_Y=int(row['CrdY']) if pd.notna(row['CrdY']) else None,
#             crd_R=int(row['CrdR']) if pd.notna(row['CrdR']) else None,
#             x_G=float(row['xG']) if pd.notna(row['xG']) else None,
#             club_name=row['Club'],
#         )

#         # Save the current team instance to the database
#         team.save()
        
#     except Exception as e:
#         print(f"Error saving row {index}: {e}")

# print("CSV data has been loaded into the Django database.")