from django.urls import path
from .views import index, spot

urlpatterns = [
    path('', index, name="spots-index"),
    path('spot-<str:numero_spot>/', spot, name="spot")
]