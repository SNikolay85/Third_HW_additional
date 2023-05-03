from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from books.models import Book


def forming(books_objects):
    books = []
    for book in books_objects:
        book_dict = {
            'name': book.name,
            'author': book.author,
            'pub_date': book.pub_date,
        }
        books.append(book_dict)
    return books

def books_view_list(request):
    books_objects = Book.objects.all()
    books = forming(books_objects)
    template = 'books/books_list.html'
    context = {
        'books': books
    }
    return render(request, template, context)


def books_page(request, pub_date):
    books_objects = Book.objects.filter(pub_date=pub_date)
    paginator = Paginator(forming(books_objects), 1)
    page = paginator.get_page(pub_date)
    print(paginator)
    template = 'books/books.html'
    context = {
        'books': forming(books_objects),
        'page': page
    }
    return render(request, template, context)

