from django.contrib.auth.models import AbstractUser, BaseUserManager
# relationship_app/models.py
from django.db import models
from django.conf import settings
# LibraryProject/bookshelf/views.py
from django.shortcuts import render
from bookshelf.models import Book  # or from .models if Book is in this app

# LibraryProject/bookshelf/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from relationship_app.models import Book  # adjust import if Book is in a different app


@login_required
@permission_required('relationship_app.can_view', raise_exception=True)
def books(request):
    """
    View to list all books.
    Only users with the 'can_view' permission can access.
    """
    books_list = Book.objects.all()
    return render(request, 'bookshelf/books.html', {'books': books_list})

def books(request):
    """
    Display a list of all books in the system.
    """
    books_list = Book.objects.all()  # Query all books
    return render(request, 'bookshelf/books.html', {'books': books_list})


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField(null=True, blank=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]

    def __str__(self):
        return self.title


# 1️⃣ Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


# 2️⃣ Custom User Model
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
