from django.urls import path
from . import views

urlpatterns = [
    path('', views.soccer, name='soccer'),
    path('squad/<str:name>', views.team_info, name = "team"),
    path('standing/',views.rankings),
    path('index/',views.blog_index)
    
]
