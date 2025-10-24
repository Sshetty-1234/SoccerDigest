from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('',views.soccer),
    path('home/',views.home),
    path('squad/<str:name>', views.team_info, name = "team"),
    path('standing/',views.rankings),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)