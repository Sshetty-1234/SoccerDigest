from django.db import models


class Team(models.Model):
    player = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    number = models.PositiveIntegerField(null=True, blank=True)  # corresponds to '#'
    nation = models.CharField(max_length=50, null=True, blank=True)
    position = models.CharField(max_length=20, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    minutes = models.PositiveIntegerField(null=True, blank=True)
    goals = models.PositiveIntegerField(null=True, blank=True)
    assists = models.PositiveIntegerField(null=True, blank=True)
    penalty_shoot_on_goal = models.PositiveIntegerField(null=True, blank=True)
    penalty_shoot = models.PositiveIntegerField(null=True, blank=True)
    total_shoot = models.PositiveIntegerField(null=True, blank=True)
    shoot_on_target = models.PositiveIntegerField(null=True, blank=True)
    yellow_cards = models.PositiveIntegerField(null=True, blank=True)
    red_cards = models.PositiveIntegerField(null=True, blank=True)
    touches = models.PositiveIntegerField(null=True, blank=True)
    dribbles = models.PositiveIntegerField(null=True, blank=True)
    tackles = models.PositiveIntegerField(null=True, blank=True)
    blocks = models.PositiveIntegerField(null=True, blank=True)
    expected_goals_xg = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.player} ({self.team})'

class club_info(models.Model):
    club_name = models.CharField(max_length=100,default = "Football F.C")
    club_id = models.IntegerField()
    club_description = models.TextField()
    club_crest = models.ImageField(default="nothing",blank=True)
    
    def __str__(self):
        return f'{self.club_name} ({self.club_crest})'
    
class soccer_buddy(models.Model):
    image = models.ImageField(default="nothing",blank=True)  
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description
    