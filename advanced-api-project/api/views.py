from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Book
from .serializers import BookSerializer
from .permissions import  IsOwnerOrReadOnly

# Create your views here.
class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # require login to create


    def perform_create(self, serializer):


        serializer.save(created_by=self.request.user)
# Extra rule requiring DB access: prevent duplicate title by same author
        title = serializer.validated_data.get("title")
        author = serializer.validated_data.get("author")

        if Book.objects.filter(title__iexact=title, author__iexact=author).exists():
            # raise ValidationError -> DRF turns into 400 response
            raise ValidationError({"title": "A book with this title and author already exists."})


class BookUpdateAPIView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        # Example business rule: published_year can't be changed to before 1900
        old = self.get_object()  # the existing Book instance
        new_year = serializer.validated_data.get("published_year", old.published_year)

        if new_year is not None and new_year < 1900:
            raise ValidationError({"published_year": "Published year must be 1900 or later."})


class BookDeleteAPIView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]



