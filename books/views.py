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

def books_view(request):
    books_objects = Book.objects.all()
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(forming(books_objects), 1)
    page = paginator.get_page(page_number)
    template = 'books/books_list.html'
    context = {
        'books': page,
        'page': page
    }
    return render(request, template, context)
