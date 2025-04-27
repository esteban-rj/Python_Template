from django.shortcuts import render
from django.http import JsonResponse
import requests

# Create your views here.
def get_pokemon(request):
    # Get the pokemon name from the request
    name = request.GET.get("name")
    #call the pokemon api
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    #return the response
    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "Pokemon not found"}, status=404)
