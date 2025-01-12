# E-commerce API

## Project Overview

The **E-commerce API** is a backend application built using **Django** and **Django REST Framework (DRF)**. It provides a set of RESTful APIs to manage products, categories, and product reviews for an e-commerce platform. The API also handles user authentication, role-based permissions, and allows users to interact with the data in a secure and efficient way.

## Features

- **User Authentication**: Register, login, and authenticate users via JWT (JSON Web Token).
- **Product Management**: Create, update, delete, and list products in the store.
- **Category Management**: Manage product categories (CRUD functionality).
- **Review System**: Users can leave reviews for products, with ratings and optional comments.
- **Pagination**: The API supports pagination for listing products and reviews.
- **Search & Filtering**: Products can be searched and filtered based on fields like name, description, price, and category.
- **Role-based Permissions**: Only admins can create, update, or delete products and categories. Regular users can interact with products and leave reviews.
  
## Technologies Used

- **Django**: The primary framework used to build the backend.
- **Django REST Framework**: Toolkit used to build the API.
- **JWT Authentication**: Used for secure user authentication.
- **Django Filters**: Allows filtering and searching of product data.
- **SQLite**: The default database used in development (can be configured for other databases like PostgreSQL).

API Endpoints
User Authentication
POST /api/auth/register/ – Register a new user.
POST /api/auth/login/ – Log in and receive a JWT token.
Products
GET /api/products/ – List all products.
POST /api/products/ – Create a new product (Admin only).
GET /api/products/{id}/ – Retrieve a product by its ID.
PUT /api/products/{id}/ – Update a product (Admin only).
DELETE /api/products/{id}/ – Delete a product (Admin only).
Categories
GET /api/categories/ – List all categories.
POST /api/categories/ – Create a new category (Admin only).
GET /api/categories/{id}/ – Retrieve a category by its ID.
PUT /api/categories/{id}/ – Update a category (Admin only).
DELETE /api/categories/{id}/ – Delete a category (Admin only).
Reviews
GET /api/reviews/ – List all reviews.
POST /api/reviews/ – Create a review for a product (Authenticated users only).
GET /api/reviews/{id}/ – Retrieve a specific review by its ID.
PUT /api/reviews/{id}/ – Update a review (Only the owner can update).
DELETE /api/reviews/{id}/ – Delete a review (Only the owner can delete).
