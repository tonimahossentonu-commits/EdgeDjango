from django.shortcuts import render, get_object_or_404
from .models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, 'library/list_books.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'library/book_detail.html', {'book': book})
