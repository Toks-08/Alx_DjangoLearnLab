from django.views.generic import DetailView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library

def book_list_view(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class BookDetailView(DetailView):
    model = Book
    template_name = 'list_books.html'  # the HTML template file
    context_object_name = 'book'