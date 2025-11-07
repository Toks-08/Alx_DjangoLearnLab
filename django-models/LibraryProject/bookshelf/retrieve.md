# Retrieve a Book From the Database

```python
from bookshelf.models import Book

# Retrieve a specific book using Django ORM
book = Book.objects.get(title="1984")
book

