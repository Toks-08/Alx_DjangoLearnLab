# Update the title of “1984” to “Nineteen Eighty-Four”
book = Book.objects.get(title="1984")   # Retrieve the book
book.title = "Nineteen Eighty-Four"     # Update the title
book.save()                             # Save changes

# Expected Output:
# The book title should now be updated in the database.
# You can verify using:
# Book.objects.get(title="Nineteen Eighty-Four")
