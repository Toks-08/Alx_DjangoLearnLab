from rest_framework import serializers
from .models import Author, Book
from rest_framework.exceptions import ValidationError
from datetime import date

#BookSerializer
# Purpose: Converts complex Book model instances into native Python datatypes
# (and then JSON) for the API response. Also handles data deserialization
# and validation for Book objects on creation/update.

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'publication_year', 'authors')

        def validate_publication_year(self, value):
            current_year = date.today().year
            if value > current_year:
                # Raise a ValidationError if the year is in the future
                raise ValidationError(
                    f"Publication year cannot be in the future. The latest valid year is {current_year}.")
            return value

#AuthorSerializer
# Purpose: Serializes Author model instances. It includes a nested
# representation of all related Book objects, providing a single,
# comprehensive view of an author and their works.

class AuthorSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=True, read_only=True)
    class Meta:
        models = Author
        fields = ['id','name', 'book']
∂