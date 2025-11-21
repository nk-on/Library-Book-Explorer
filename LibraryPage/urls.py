from django.urls import path
from .views import allBooks,book
urlpatterns = [
    path('',allBooks,name='book-page'),
    path('<str:book>',book,name='book-page')
]
