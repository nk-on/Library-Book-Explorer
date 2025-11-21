from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

books = {
    "harry-potter": {"title": "Harry Potter", "author": "J.K. Rowling", "rating": 9},
    "hobbit": {"title": "The Hobbit", "author": "J.R.R. Tolkien", "rating": 8},
    "gatsby": {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "rating": 7,
    },
}


# Create your views here.
def allBooks(request):
    booksListing = ''
    for key in books:
        booksListing+=f"<li>{key}</li>"
    return HttpResponse(f"<ul>{booksListing}</ul>")
def book(request,book):
    try:
        return HttpResponse(f"{books[book]}")
    except:
        return HttpResponseNotFound("<h1>404 Not found</h1>")
