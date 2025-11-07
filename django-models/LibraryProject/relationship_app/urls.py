from django.urls import path
from .views import BookDetailView, book_list_view

urlpatterns = [
    path('book/', BookDetailView.as_view(), name = 'book' ),
    path('lib/', book_list_view,),
]