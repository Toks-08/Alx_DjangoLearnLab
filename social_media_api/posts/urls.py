from .views import PostView, CommentView, FeedListView, LikePostView, UnlikePostView
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'post', PostView)
router.register(r'comment', CommentView)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedListView.as_view(), name = 'user-feed'),
    path('post/<int:pk>/like/', LikePostView.as_view()),
    path('post/<int:pk>/unlike/', UnlikePostView.as_view())
    
]