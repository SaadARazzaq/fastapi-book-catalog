from fastapi import Body, FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class Book():
    id: int
    title: str
    author: str
    category: str
    price: int
    quantity: int
    rating: int

    def __init__(self, id, title, author, category, price, quantity, rating):
        self.id = id
        self.title = title
        self.author = author
        self.category= category
        self.price = price
        self.quantity = quantity
        self.rating = rating

class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length = 3)
    author: str = Field(min_length= 1)
    category: str = Field(min_length = 3)
    price: int = Field(gt=1)
    quantity: int = Field(gt=0)
    rating: int = Field(gt=0, lt=5)

BOOKS = [
    Book(1, "Holy Quran", "Allah Almighty", "Religious", 50, 112, 5),
    Book(2, "1984", "George Orwell", "Fiction", 20, 50, 4),
    Book(3, "To Kill a Mockingbird", "Harper Lee", "Fiction", 15, 75, 4),
    Book(4, "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 18, 60, 4),
    Book(5, "The Catcher in the Rye", "J.D. Salinger", "Fiction", 16, 55, 3),
    Book(6, "Pride and Prejudice", "Jane Austen", "Fiction", 14, 70, 4),
    Book(7, "The Hobbit", "J.R.R. Tolkien", "Fantasy", 25, 45, 5),
    Book(8, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fantasy", 22, 65, 5)
]

# Get Request --------------------
# Get Request --------------------
# Get Request --------------------
@app.get("/Books")
async def read_all_books():
    if len(BOOKS) == 0:
        return { "Message" : "No Books found in the system " }
    else:
        return BOOKS
    

# Post Request --------------------

@app.post("/create_book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(new_book)