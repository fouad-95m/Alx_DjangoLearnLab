from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    Retrieve all books.
    Accessible to everyone (read-only access).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single book by its ID.
    Accessible to everyone (read-only access).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class BookCreateView(generics.CreateAPIView):
    """
    Add a new book with custom validation and logic.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Example: Add custom logic (e.g., automatically set the logged-in user)
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book with custom logic.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Example: Add logging or other logic before saving
        serializer.save()



class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book by its ID.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

 ["ListView", "DetailView", "CreateView", "UpdateView", "DeleteView"]
 ["from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated"]
["from django_filters import rest_framework"]
