from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('books/', list_books, name='list_books'),                  # FBV
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    # Authentication URLs
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='relationship_app/login.html'
    ), name='login'),

    path('accounts/logout/', auth_views.LogoutView.as_view(
        next_page='login'  # redirect to login after logout
    ), name='logout'),

    path('accounts/register/', views.register, name='register'),
]