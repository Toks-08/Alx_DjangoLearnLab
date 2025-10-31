# Delete the book titled "Nineteen Eighty-Four"
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()   # Deletes the object

# Confirm deletion by fetching all books again
Book.objects.all()
