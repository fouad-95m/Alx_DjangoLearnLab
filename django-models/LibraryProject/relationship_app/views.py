from django.shortcuts import render, redirect,get_object_or_404
from relationship_app.models import Book , Library
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .models import Book
from .forms import BookForm # type: ignore


# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

["relationship_app/list_books.html"]
["relationship_app/library_detail.html", "from .models import Library"]
["from django.views.generic.detail import DetailView"]
["from .views import list_books"]
# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'


# Login view (uses built-in LoginView)
class UserLoginView(LoginView):
    template_name = 'login.html'

# Logout view (uses built-in LogoutView)
class UserLogoutView(LogoutView):
    template_name = 'logout.html'

# Registration view (custom form)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately after registration
            return redirect('list_books')  # Redirect to the books list or another page
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


# Function to check if the user is an Admin
def is_admin(user):
    return user.profile.role == 'Admin'

# Function to check if the user is a Librarian
def is_librarian(user):
    return user.profile.role == 'Librarian'

# Function to check if the user is a Member
def is_member(user):
    return user.profile.role == 'Member'

# Admin view - only accessible to Admin users
@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome, Admin!")

# Librarian view - only accessible to Librarians
@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Welcome, Librarian!")

# Member view - only accessible to Members
@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Welcome, Member!")



# Add a book - only users with 'can_add_book' permission can access this view
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to the list of books or another view
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

# Edit a book - only users with 'can_change_book' permission can access this view
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to the list of books or another view
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

# Delete a book - only users with 'can_delete_book' permission can access this view
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')  # Redirect to the list of books or another view
    return render(request, 'relationship_app/delete_book.html', {'book': book})
