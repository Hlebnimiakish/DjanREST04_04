from django.urls import path
from REST.view import someData

urlpatterns = [
    path('restdata/', someData),
]