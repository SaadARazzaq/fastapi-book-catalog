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
    rating: int = Field(gt=0, le=5)

    class Config:
        json_schema_extra = {
            "example" : {
                "title" : "Book Title",
                "author" : "Saad Abdur Razzaq",
                "category" : "Book Category",
                "price" : 10,
                "quantity" : 10,
                "rating" : 5
            }
        }


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

@app.get("/Books")
async def read_all_books():
    if len(BOOKS) == 0:
        return { "Message" : "No Books found in the system " }
    else:
        return BOOKS
    
# Get Request with dynamic url to fetch only single book --------------------

@app.get("/Books/id/{Book_id}")
async def read_certain_book_by_id(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book
        else:
            return { "Message" : "No Books found in the system " }
        
# Get Request with dynamic url to fetch books by certain ratings --------------------

@app.get("/Books/rating/{Book_rating}")
async def read_certain_book_by_rating(book_rating: int):
    BOOKS_WITH_RATING_X = []
    for book in BOOKS:
        if book.rating == book_rating:
            BOOKS_WITH_RATING_X.append(book)
    if len(BOOKS_WITH_RATING_X) == 0:
        return { "Message" : "No Books found in the system " }
    else:
        return BOOKS_WITH_RATING_X

# Post Request --------------------

@app.post("/create_book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(get_book_id(new_book))

def get_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book