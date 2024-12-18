import csv
from django.core.management.base import BaseCommand
from PL.models import Team

class Command(BaseCommand):
    help = "Import team data from a CSV file into the Team model"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help="Path to the CSV file")

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        
        try:
            with open(csv_file, 'r') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    try:
                        # Map CSV columns to model fields
                        name = row['Name'].strip() if row['Name'] else None
                        nation = row['Nation'].strip() if row['Nation'] else None
                        pos = row['Pos'].strip() if row['Pos'] else None
                        club_name = row['Club'].strip() if row['Club'] else None

                        # Ensure numeric fields are properly converted or set to defaults
                        age = self.safe_int(row['Age'], default=0)
                        gp = self.safe_int(row['Games Played'], default=0)
                        ast = self.safe_int(row['Ast'], default=0)
                        crd_Y = self.safe_int(row['CrdY'], default=0)
                        crd_R = self.safe_int(row['CrdR'], default=0)
                        x_G = self.safe_float(row['xG'], default=0.0)

                        # Skip row if essential fields are missing
                        if not all([name, nation, pos, club_name]):
                            self.stdout.write(self.style.WARNING(f"Skipping row with missing required fields: {row}"))
                            continue

                        # Create team entry
                        Team.objects.create(
                            name=name,
                            nation=nation,
                            pos=pos,
                            age=age,
                            gp=gp,
                            ast=ast,
                            crd_Y=crd_Y,
                            crd_R=crd_R,
                            x_G=x_G,
                            club_name=club_name
                        )

                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f"Error processing row {row}: {e}"))

            self.stdout.write(self.style.SUCCESS("Data imported successfully!"))
        
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred while opening the file: {e}"))

    def safe_int(self, value, default=None):
        """Safely convert a value to an integer."""
        try:
            return int(value) if value.strip() else default
        except ValueError:
            return default

    def safe_float(self, value, default=None):
        """Safely convert a value to a float."""
        try:
            return float(value) if value.strip() else default
        except ValueError:
            return default
