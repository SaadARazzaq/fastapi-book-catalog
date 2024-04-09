# FastAPI Book Catalog API

This is a FastAPI-based RESTful API for managing books. It allows you to perform CRUD operations on a collection of books stored in memory. The API includes endpoints for retrieving all books, fetching a single book by ID, fetching books by rating, fetching books by published date, creating a new book, updating an existing book, and deleting a book.

## Requirements

- Python
- FastAPI
- Pydantic
- Starlette

## Installation

1. Clone this repository.
2. Navigate to the project directory.
3. Create a virtual environment: `python -m venv venv`.
4. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
5. Install the required dependencies.

## Usage

1. Run the FastAPI server: `uvicorn main:app --reload`.
2. Open your browser, swagger UI or an API client like Postman.
3. Use the following endpoints:

### Endpoints

- `GET /Books`: Retrieve all books.
- `GET /Books/{Book_id}`: Retrieve a specific book by ID.
- `GET /Books/rating?book_rating={rating}`: Retrieve books by rating.
- `GET /Books/published_date?book_published_year={year}`: Retrieve books by published year.
- `POST /create_book`: Create a new book (requires JSON payload).
- `PUT /Books/update_book`: Update an existing book (requires JSON payload).
- `DELETE /Books/delete_book/{book_id}`: Delete a book by ID.

### JSON Payload Example for POST and PUT Requests

```json
{
  "title": "Book Title",
  "author": "Author Name",
  "category": "Book Category",
  "published_date": 2000,
  "price": 20,
  "quantity": 50,
  "rating": 4
}
```

### Response Status Codes

- 200 OK: Successful GET request.
- 201 Created: Successful POST request.
- 204 No Content: Successful PUT or DELETE request.
- 404 Not Found: Resource not found.

## JSON Schema Example

The API uses Pydantic for request body validation. Here's an example JSON schema for creating a new book:

```json
{
  "title": "Book Title",
  "author": "Author Name",
  "category": "Book Category",
  "published_date": 2000,
  "price": 20,
  "quantity": 50,
  "rating": 4
}
```

**NOTE: I HAVE USED PYDANTIC v2. YOU CAN SEE BELOW AND FOLLOW IT IN CASE U PLAN TO USE PYDANTIC v1**

![image](https://github.com/SaadARazzaq/fastapi-book-catalog/assets/123338307/72d79ae8-579b-4d17-835b-8674026b906f)
