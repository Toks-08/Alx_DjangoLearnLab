from django.views.generic import DetailView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library

def book_list_view(request):
    books = Book.objects.all()
    output = "<h2>List of Books</h2>"
    for book in books:
        output += f"<p><strong>{book.title}</strong> by {book.author.name}</p>"
    return HttpResponse(output)

class BookDetailView(DetailView):
    model = Book
    template_name = 'list_books.html'  # the HTML template file
    context_object_name = 'book'