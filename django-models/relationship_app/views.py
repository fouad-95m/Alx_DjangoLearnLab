from django.shortcuts import render
from LibraryProject import relationship_app
from .models import Book
from django.views.generic import DetailView
from .models import Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})


# Class-based view to display details of a library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
relationship_app/list_books.html
relationship_app/library_detail.html