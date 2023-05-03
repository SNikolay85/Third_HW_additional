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


def forming_date(books_objects):
    books = []
    for book in books_objects:
        book_dict = {
            str(book.pub_date):{
                'name': book.name,
                'author': book.author,
            }
        }
        books.append(book_dict)
    return books
# content = [
#     {'pub_date':{'name': book.name, 'author': book.author}}
# ]

def books_view_list(request):
    books_objects = Book.objects.all()
    books = forming(books_objects)
    template = 'books/books_list.html'
    context = {
        'books': books
    }
    return render(request, template, context)


def books_page(request, pub_date):
    page_number = request.path
    #books_objects = Book.objects.filter(pub_date=pub_date)
    books_objects = Book.objects.all()
    paginator = Paginator(forming_date(books_objects), 5)
    page = paginator.get_page(page_number)
    previous_page = 30
    next_page = 50
    print(page_number)
    print(forming_date(books_objects))
    template = 'books/books.html'
    context = {
        'books': page,#forming_date(books_objects),
        'pub_date': pub_date,
        'page': page,
        'previous_page': previous_page,
        'next_page': next_page
    }
    return render(request, template, context)

