from .models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "Chinua Achebe"
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)

print("Books by", author_name)
for book in books:
    print("-", book.title)


# List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = Book.objects.filter(library=library)

print("\nBooks in", library_name)
for book in books_in_library:
    print("-", book.title)


# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print("\nThe librarian for", library_name, "is", librarian.name)
