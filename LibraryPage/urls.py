from django.urls import path
from .views import allBooks,book
urlpatterns = [
    path('',allBooks),
    path('<str:book>',book)
]
