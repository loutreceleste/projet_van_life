from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def index(request):
    return render(request, "spots-index.html", context={"prenom": "Edward"})

def spot(request, numero_spot):
    return render(request, "spot.html", context={"prenom": "Edward"})