from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password123')

        # Create some sample books
        self.book1 = Book.objects.create(title='Book One', author='Alice', published_year=2020)
        self.book2 = Book.objects.create(title='Book Two', author='Bob', published_year=2021)

    # ------------------------------
    # Test List and Retrieve
    # ------------------------------
    def test_list_books(self):
        url = reverse('book_list')  # Make sure your URL names match
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        url = reverse('book_detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    # ------------------------------
    # Test Create
    # ------------------------------
    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='password123')  # Authenticate
        url = reverse('book_create')
        data = {'title': 'Book Three', 'author': 'Charlie', 'published_year': 2022}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        url = reverse('book_create')
        data = {'title': 'Book Three', 'author': 'Charlie', 'published_year': 2022}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Permission enforced

    # ------------------------------
    # Test Update
    # ------------------------------
    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='password123')
        url = reverse('book_update', args=[self.book1.id])
        data = {'title': 'Updated Book One', 'author': 'Alice', 'published_year': 2020}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book One')

    # ------------------------------
    # Test Delete
    # ------------------------------
    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='password123')
        url = reverse('book_delete', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ------------------------------
    # Test Filtering, Searching, Ordering
    # ------------------------------
    def test_filter_books_by_author(self):
        url = reverse('book_list') + '?author=Alice'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Alice')

    def test_search_books_by_title(self):
        url = reverse('book_list') + '?search=Two'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book Two')

    def test_order_books_by_published_year_desc(self):
        url = reverse('book_list') + '?ordering=-published_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['published_year'], 2021)
