############################################################
# ✅ CREATE — Add a new book
############################################################

from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book  # Expected: <Book: 1984 by George Orwell (1949)>


############################################################
# ✅ READ — Retrieve all books
############################################################

Book.objects.all()
# Expected: <QuerySet [<Book: 1984 by George Orwell (1949)>]>


############################################################
# ✅ UPDATE — Change book title from "1984" to "Nineteen Eighty-Four"
############################################################

book = Book.objects.get(title="1984")     # Retrieve book
book.title = "Nineteen Eighty-Four"       # Update title
book.save()                               # Save changes

Book.objects.get(title="Nineteen Eighty-Four")
# Expected: <Book: Nineteen Eighty-Four by George Orwell (1949)>


############################################################
# ✅ DELETE — Remove the book
############################################################

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# Expected: (1, {'bookshelf.Book': 1})


############################################################
# ✅ READ AGAIN — Confirm deletion
############################################################

Book.objects.all()
# Expected: <QuerySet []>
