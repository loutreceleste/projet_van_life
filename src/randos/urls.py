from django.urls import path
from .views import index, rando

urlpatterns = [
    path('', index, name="randos-index"),
    path('rando-<str:numero_rando>/', rando, name="rando")
]
