# Advanced API Project

## Overview
A Django REST Framework project demonstrating CRUD operations using generic views and custom permissions.

## Endpoints
- `GET /api/books/`: Retrieve all books.
- `GET /api/books/<int:pk>/`: Retrieve details of a specific book by ID.
- `POST /api/books/create/`: Add a new book (authenticated users only).
- `PUT /api/books/<int:pk>/update/`: Update an existing book (authenticated users only).
- `DELETE /api/books/<int:pk>/delete/`: Delete a book (authenticated users only).

## Permissions
- List and Detail views: Accessible to everyone (read-only for unauthenticated users).
- Create, Update, and Delete views: Restricted to authenticated users.

## Testing
- Use Postman or cURL to test endpoints.
- Ensure proper credentials for restricted views.
