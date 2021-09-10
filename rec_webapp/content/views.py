from django.shortcuts import render
from django.http import HttpResponse

import requests


def home_page(request):

    print("REQUEST: ", request)

    url = "https://jikan1.p.rapidapi.com/search/anime"

    querystring = {"q": "sword"}

    headers = {
        'x-rapidapi-host': "jikan1.p.rapidapi.com",
        'x-rapidapi-key': "a9a273731fmshe967bab5c6f764cp1b2dedjsne77e350e643d"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    return HttpResponse(response.text)
    # return 0
