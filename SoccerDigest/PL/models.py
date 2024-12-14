from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)  
    nation = models.CharField(max_length=50)
    pos = models.CharField(max_length=10)
    age = models.IntegerField()
    gp = models.IntegerField()  # Games played
    ast = models.IntegerField()  # Assists
    crd_Y = models.IntegerField()  # Yellow cards
    crd_R = models.IntegerField()  # Red cards
    x_G = models.DecimalField(max_digits=5, decimal_places=2)  # Expected goals
    club_name = models.CharField(max_length=100) 
    
    def __str__(self):
        return f'{self.name} ({self.club_name})'
    
class club_info(models.Model):
    club_name = models.CharField(max_length=100,default = "Football F.C")
    club_id = models.IntegerField()
    club_description = models.TextField()
    club_crest = models.ImageField(default="nothing",blank=True)
    
    def __str__(self):
        return f'{self.club_name} ({self.club_crest})'
    
class Category(models.Model):
    name = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self):
        return f'{self.name}'
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    
    def __str__(self):
        return f'{self.title}'
    
class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    