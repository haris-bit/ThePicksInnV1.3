from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
import json



def get_top_20_players():
    response = requests.get('https://mybackendnba-e0bd8ae9accb.herokuapp.com/advance-stats/')
    print('Top 20 Players Status Code:', response.status_code)
    if response.status_code == 200:
        return response.json()
    return None

def get_leaderboard_data():
    response = requests.get('https://mybackendnba-e0bd8ae9accb.herokuapp.com/api/leaderboard-list/')
    print('Leaderboard Data Status Code:', response.status_code)
    if response.status_code == 200:
        return response.json()
    return None

@api_view(['GET'])
def top_20_players(request):
    # Get data for top 20 players
    data1 = get_top_20_players()

    # Check if the response is successful
    if data1 is not None:
        # Pass the data to the template
        context = {'data1': data1}
        return render(request, 'myapp/index.html', context)
    else:
        # Pass status codes to the template for debugging
        context = {'status_code': f'Top 20 players data retrieval failed'}
        return render(request, 'myapp/index.html', context)

@api_view(['GET'])
def leaderboard(request):
    # Get data for leaderboard
    data2 = get_leaderboard_data()

    # Check if the response is successful
    if data2 is not None:
        # Sort the data2 by 'accuracy', 'correct_picks_count', and 'per_percentage'
        data2 = sorted(data2, key=lambda k: (k['accuracy'], k['correct_picks_count'], k['per_percentage']), reverse=True)

        # Pass the data to the template
        context = {'data2': data2}
        return render(request, 'myapp/leaderboard.html', context)
    else:
        # Pass status codes to the template for debugging
        context = {'status_code': f'Leaderboard data retrieval failed'}
        return render(request, 'myapp/leaderboard.html', context)

