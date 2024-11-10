from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian

# Example usage
if __name__ == "__main__":
    author_books = books_by_author("J.K. Rowling")
    print("Books by J.K. Rowling:")
    for book in author_books:
        print(book.title)

    library_books = books_in_library("Central Library")
    print("\nBooks in Central Library:")
    for book in library_books:
        print(book.title)

    librarian = librarian_for_library("Central Library")
    print(f"\nLibrarian for Central Library: {librarian.name}")
