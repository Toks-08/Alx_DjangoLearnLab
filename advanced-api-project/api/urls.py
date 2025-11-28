from django.urls import path
from .views import (
    BookListAPIView, BookDetailAPIView, BookCreateAPIView,
    BookUpdateAPIView, BookDeleteAPIView
)

urlpatterns = [
    path('', BookListAPIView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailAPIView.as_view(), name='book_detail'),
    path('create/', BookCreateAPIView.as_view(), name='book_create'),
    path('<int:pk>/update/', BookUpdateAPIView.as_view(), name='book_update'),
    path('<int:pk>/delete/', BookDeleteAPIView.as_view(), name='book_delete'),
]
