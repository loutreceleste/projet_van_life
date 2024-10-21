from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def index(request):
    return render(request, "randos-index.html", context={"prenom": "Edward"})

def rando(request, numero_rando):
    return render(request, "rando.html", context={"prenom": "Edward"})