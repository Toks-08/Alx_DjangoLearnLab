# LibraryProject/bookshelf/forms.py

from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    """
    Example form for creating or updating a Book instance.
    Uses Django's ModelForm for automatic validation.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']  # include the fields you want in the form
