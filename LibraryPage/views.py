from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

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
    booksListing = ""
    bookTitles = list(books.keys())
    context = {
        "bookTitles":bookTitles,
    }
    return render(request,'LibraryPage/LibraryPage.html',context)


def book(request, book):
    titles = list(books[book].keys())
    try:
        individualBook = books[book]
        context = {"book":individualBook,"titles":titles}
        return render(request,'LibraryPage/BookPage.html',context)
    except:
        return render('<h2>404 not found</h2>')
