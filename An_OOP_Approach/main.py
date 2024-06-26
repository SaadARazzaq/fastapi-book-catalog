from fastapi import FastAPI, Body, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from starlette import status

'''
Note: Some Important things to know:
# Validation for query parameters is applied to: "/Books/Published_Date"
# Validation for path parameters is applied to: "/Books/Certain_book/{id}"
'''

'''
NOTE: STATUS CODE RESPONSES
- For GET requests => HTTP_200_OK (Because we are returning something)
- For POST requests => HTTP_201_CREATED (Because we are creating something and NOT returning)
- For PUT, DELETE requests => HTTP_204_NO_CONTENT (Because we are NOT creating OR returning something but updating/enhancing our application)

'''

app = FastAPI()

class Book():
    id: int
    title: str
    author: str
    category: str
    published_date: int
    price: int
    quantity: int
    rating: int

    def __init__(self, id, title, author, category, published_date, price, quantity, rating):
        self.id = id
        self.title = title
        self.author = author
        self.category= category
        self.published_date = published_date
        self.price = price
        self.quantity = quantity
        self.rating = rating

class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length = 3)
    author: str = Field(min_length= 1)
    category: str = Field(min_length = 3)
    published_date: int = Field(gt=999)
    price: int = Field(gt=1)
    quantity: int = Field(gt=0)
    rating: int = Field(gt=0, le=5)

    class Config:
        json_schema_extra = {
            "example" : {
                "title" : "Book Title",
                "author" : "Saad Abdur Razzaq",
                "category" : "Book Category",
                "published_date" : 2002,
                "price" : 10,
                "quantity" : 10,
                "rating" : 5
            }
        }


BOOKS = [
    Book(1, "Holy Quran", "Allah Almighty", "Religious", 1440, 50, 112, 5),
    Book(2, "1984", "George Orwell", "Fiction", 1984, 20, 50, 4),
    Book(3, "To Kill a Mockingbird", "Harper Lee", "Fiction", 2000, 15, 75, 4),
    Book(4, "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 2005, 18, 60, 4),
    Book(5, "The Catcher in the Rye", "J.D. Salinger", "Fiction", 2010, 16, 55, 3),
    Book(6, "Pride and Prejudice", "Jane Austen", "Fiction", 2017, 14, 70, 4),
    Book(7, "The Hobbit", "J.R.R. Tolkien", "Fantasy", 2007, 25, 45, 5),
    Book(8, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fantasy", 2019, 22, 65, 5)
]

# Get Request --------------------

@app.get("/Books", status_code=status.HTTP_200_OK)
async def read_all_books():
    if len(BOOKS) == 0:
        # return { "Message" : "No Books found in the system " }
        raise HTTPException(status_code=404, detail='Item Not Found')
    else:
        return BOOKS
    
# Get Request with dynamic url to fetch only single book --------------------

@app.get("/Books/{Book_id}", status_code=status.HTTP_200_OK)
async def read_certain_book_by_id(book_id: int = Path(gt= 0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
        else:
            # return { "Message" : "No Books found in the system " }
            raise HTTPException(status_code=404, detail='Item Not Found')
        
# Get Request with dynamic url to fetch books by certain ratings --------------------

@app.get("/Books/rating", status_code=status.HTTP_200_OK)
async def read_certain_book_by_rating(book_rating: int = Query(gt= 0, lt= 6)):
    RETURN_BOOKS = []
    for book in BOOKS:
        if book.rating == book_rating:
            RETURN_BOOKS.append(book)
    if not RETURN_BOOKS:
        raise HTTPException(status_code=404, detail='No books found for the given rating')
    return RETURN_BOOKS
    
# Get Request with dynamic url to fetch books by Published Year --------------------

@app.get("/Books/published_date", status_code=status.HTTP_200_OK)
async def read_books_by_published_date(book_published_year: int = Query(gt= 999)):
    RETURN_BOOKS = []
    for book in BOOKS:
        if book.published_date == book_published_year:
            RETURN_BOOKS.append(book)
    if len(RETURN_BOOKS) == 0:
        # return { "Message" : "No Books found in the system " }
        raise HTTPException(status_code=404, detail='Item Not Found')
    else:
        return RETURN_BOOKS

# Post Request --------------------

@app.post("/create_book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(get_book_id(new_book))

def get_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book

# Put Request --------------------

@app.put("/Books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    flag = 0
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            flag = 1
            BOOKS[i] = book
    if flag == 0:
        # return { "Message" : "No Books found to Delete " }
        raise HTTPException(status_code=404, detail='Item Not Found')

# Delete Request --------------------

@app.delete("/Books/delete_book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt= 0)):
    flag = 0
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            flag = 1
            BOOKS.pop(i)
            break
    if flag == 0:
        # return { "Message" : "No Books found to Delete " }
        raise HTTPException(status_code=404, detail='Item Not Found')
    