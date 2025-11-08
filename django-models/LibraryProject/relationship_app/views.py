from django.http import HttpResponse
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    # Optionally, add books to the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # all books for this library
        return context


def list_books(request):
    books = Book.objects.all()
    output = ""
    for book in books:
        output += f"Title: {book.title}, Author: {book.author}\n"
    return HttpResponse(output, content_type="text/plain")
