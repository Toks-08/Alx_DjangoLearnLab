# Delete a Book From the Database

```python
from bookshelf.models import Book

# Retrieve the book you want to delete
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion
Book.objects.all()

