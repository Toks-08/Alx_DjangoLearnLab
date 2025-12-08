from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CommentUpdateView, CommentDeleteView
from . import views

urlpatterns = [
    #path('login/', auth_views.LoginView.as_view(template_name= 'blog/login.html'), name='blog/login'),
    #path('logout/', auth_views.LogoutView.as_view(next_page= 'login')),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/comments/new', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('posts/<int:post_id>/comments/new/', views.add_comment, name='add-comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-edit'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]


