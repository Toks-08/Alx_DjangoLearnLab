from django.shortcuts import render
from .serializers import BookSerializer
from rest_framework import generics, viewsets
from .models import Book
from rest_framework import permissions
# Create your views here.

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # api/views.py (Advanced Example)
    from rest_framework import viewsets
    from rest_framework import permissions

    class BookViewSet(viewsets.ModelViewSet):
        queryset = Book.objects.all()
        serializer_class = BookSerializer

        # 🌟 Customizing permissions based on the action 🌟
        def get_permissions(self):
            # Allow anyone to read (GET, HEAD, OPTIONS)
            if self.action in ['list', 'retrieve']:
                permission_classes = [permissions.AllowAny]

            # Require admin privileges for creating, updating, or deleting
            else:  # 'create', 'update', 'partial_update', 'destroy'
                permission_classes = [permissions.IsAdminUser]

            return [permission() for permission in permission_classes]
