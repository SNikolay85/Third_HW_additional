from django.shortcuts import render
from books.models import Book


def books_view_list(request):
    books_objects = Book.objects.all()
    template = 'books/books_list.html'
    context = {
        'books': books_objects
    }
    return render(request, template, context)


def books_page(request, pub_date):
    books_objects = Book.objects.filter(pub_date__exact=pub_date)
    previous_page = Book.objects.filter(pub_date__lt=pub_date).first()
    next_page = Book.objects.filter(pub_date__gt=pub_date).first()
    template = 'books/books_list.html'
    context = {
        'books': books_objects,
        'previous_page': previous_page,
        'next_page': next_page
    }
    return render(request, template, context)

