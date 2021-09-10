from django.shortcuts import render
from django.http import HttpResponse

import os
import requests

def home_page(request):

    print("REQUEST: ", request)

    url = "https://jikan1.p.rapidapi.com/search/anime"

    querystring = {"q": "sword"}

    headers = {
        'x-rapidapi-host': "jikan1.p.rapidapi.com",
        'x-rapidapi-key': os.getenv('X_RAPIDAPI_KEY')
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    return HttpResponse(response.text)
    # return 0
