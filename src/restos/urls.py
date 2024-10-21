from django.urls import path
from .views import index, resto

urlpatterns = [
    path('', index, name="restos-index"),
    path('resto-<str:numero_resto>/', resto, name="resto")
]