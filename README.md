# fastapi-book-catalog

## Overview

This FastAPI-based Bookstore API provides endpoints to manage a collection of books. The API allows users to perform CRUD (Create, Read, Update, Delete) operations on books in the inventory. It supports features like fetching all books, fetching books by title, author, or category, creating new books, updating existing books, and deleting books.

## Endpoints

### GET /books

Fetches all books available in the inventory.

### GET /books/{book_title}

Fetches a specific book by its title.

### GET /books/?category={category}

Fetches books by a specified category.

### GET /books/{book_author}/?category={category}

Fetches books by a specified author and category.

### POST /books/create_book

Creates a new book in the inventory. Expects a JSON payload with book details.

### PUT /books/update_book

Updates an existing book in the inventory. Expects a JSON payload with updated book details.

### DELETE /books/delete_book/{book_title}

Deletes a book from the inventory based on its title.

### GET /Books/{author}/

Fetches all books from a specific author.

## Data Model

The book data is stored in memory using a Python list named `BOOKS`. Each book is represented as a dictionary with the following keys:
- `title`: Title of the book
- `author`: Author of the book
- `category`: Category of the book
- `ISBN`: ISBN number of the book
- `price`: Price of the book
- `quantity`: Quantity of the book available in the inventory

## Usage

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the FastAPI application using `uvicorn main:app --reload`.
4. Access the API endpoints using a tool like Postman or by sending HTTP requests directly.

## Assessment Endpoint

The provided assessment endpoint `GET /Books/{author}/` fetches all books from a specific author. It takes the author's name as a path parameter and returns a list of books authored by that author.
