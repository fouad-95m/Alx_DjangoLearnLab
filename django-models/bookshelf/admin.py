from django.contrib import admin
from .models import Book

# Register the Book model with the admin interface
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display title, author, and publication year in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Enable search functionality for title and author
    search_fields = ('title', 'author')
    
    # Add filter options for publication year
    list_filter = ('publication_year',)
