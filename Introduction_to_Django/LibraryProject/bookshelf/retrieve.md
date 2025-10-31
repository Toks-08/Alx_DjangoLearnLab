# Retrieve and Display Book Attributes

The following Python commands retrieve the first book object from the QuerySet and display its individual attributes:

```python
book_instance = books.first()

print(f"Title: {book_instance.title}")
print(f"Author: {book_instance.author}")
print(f"Publication Year: {book_instance.publication_year}")

# Expected Output:
# Title: 1984
# Author: George Orwell
# Publication Year: 1949
