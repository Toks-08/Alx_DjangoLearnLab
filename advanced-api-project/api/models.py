from django.db import models

# Create your models here.

# Author Model
# Purpose: Represents a writer or contributor.
# It holds the biographical details for each author.
class Author(models.Model):
    name = models.CharField(max_length=100)
#Book Model
# Purpose: Represents a single published work.
# It links back to the Author and includes details about the publication.
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)



    def __str__(self):
        return self.title

