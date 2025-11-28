from django.urls import path
from .views import (
    ListView, DetailView, CreateView,
    UpdateView, DeleteView
)

urlpatterns = [
    path('books/', ListView.as_view(), name='book_list'),
    path('<int:pk>/',DetailView.as_view(), name='book_detail'),
    path('books/create/', CreateView.as_view(), name='book_create'),
    path('books/update/', UpdateView.as_view(), name='book_update'),
    path('books/delete/', DeleteView.as_view(), name='book_delete'),
]
