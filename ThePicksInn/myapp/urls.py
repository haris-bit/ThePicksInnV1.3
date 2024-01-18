from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path


urlpatterns = [
    # home path should be deleted (the one below this comment)
    # path('home/', views.top_20_players, name='top_20_players'),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    # path('player_efficiency_ratings/<str:username>/', views.player_efficiency_ratings, name='player_efficiency_ratings'),
]

urlpatterns = format_suffix_patterns(urlpatterns)