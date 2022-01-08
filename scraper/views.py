from django.shortcuts import render
from datetime import datetime
from django.contrib import messages
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import ScraperDetails
import requests

def get_meaning(obj):
    meaning = obj[0]['meanings'][0]['definitions'][0]['definition']
    return meaning

def get_info(word):

    url = "https://api.dictionaryapi.dev/api/v2/entries/en/{0}".format(word)
    response = requests.get(url)

    if response.status_code == 200:
        info = response.json()
        return get_meaning(info)

@ensure_csrf_cookie
def parse_info(request):
    word = request.POST.get('word')
    meaning = get_info(word)
    param = {'word': word, 'meaning': meaning}
    return render(request, "base.html", param)

