from .views import PostView, CommentView
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'post', PostView)
router.register(r'comment', CommentView)

urlpatterns = [
    path('', include(router.urls)),
    
]