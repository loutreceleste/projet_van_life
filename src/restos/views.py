from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def index(request):
    return render(request, "restos-index.html", context={"prenom": "Edward"})

def resto(request, numero_resto):
    return render(request, "resto.html", context={"prenom": "Edward"})