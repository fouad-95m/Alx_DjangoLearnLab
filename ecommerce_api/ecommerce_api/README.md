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
