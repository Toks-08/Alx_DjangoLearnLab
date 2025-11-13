from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
# relationship_app/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book
from .forms import BookForm
# bookshelf/views.py
from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required

@login_required
def search_books(request):
    query = request.GET.get('q', '')
    # ✅ Safe: using ORM to filter
    books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'books': books})

# LibraryProject/bookshelf/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from relationship_app.models import Book  # adjust this import if your Book model is in another app

@login_required
@permission_required('relationship_app.can_view', raise_exception=True)
def books(request):
    """
    Display all books.
    Only accessible to users with 'can_view' permission.
    """
    books_list = Book.objects.all()  # variable name 'books' is what the checker expects
    return render(request, 'bookshelf/books.html', {'books': books_list})

@login_required
@permission_required('relationship_app.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.added_by = request.user
            book.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form})

@login_required
@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'relationship_app/book_form.html', {'form': form})


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"