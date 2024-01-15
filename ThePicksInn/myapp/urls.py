from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path


urlpatterns = [
    path('', views.top_20_players, name='top_20_players'),
    path('home/', views.top_20_players, name='top_20_players'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]

urlpatterns = format_suffix_patterns(urlpatterns)