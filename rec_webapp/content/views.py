from django.shortcuts import render
from django.http import HttpResponse

import os
import requests


base_url = "https://jikan1.p.rapidapi.com/"

headers = {
    'x-rapidapi-host': "jikan1.p.rapidapi.com",
    'x-rapidapi-key': os.getenv('x_rapidapi_key')
}


def search_anime(query: str):
    url = base_url + "/search/anime"
    querystring = {"q": query}
    return requests.request("GET", url, headers=headers, params=querystring)


def top_anime(page: int):
    url = base_url + "/top/anime/" + str(page) + "/airing"
    return requests.request("GET", url, headers=headers)


def home_page(request):
    response = top_anime(1)
    return render(request, 'index.html', {'content': response.text})
