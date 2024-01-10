from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
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
        return render(request, 'myapp/index.html', context)
    else:
        # Pass status codes to the template for debugging
        context = {'status_code': f'Leaderboard data retrieval failed'}
        return render(request, 'myapp/index.html', context)






@api_view(['GET', 'POST'])
def drink_list(request, format=None):

    # get all the drinks
    # serialize them
    # return json
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data)
    

    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):

    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
   
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    