from django.urls import path
from .views import allBooks
urlpatterns = [
    path('',allBooks)
]
