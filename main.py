from fastapi import Body, FastAPI

app = FastAPI()


BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science', 'ISBN': '1234567890', 'price': '$50', 'quantity': 5},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science', 'ISBN': '1234567891', 'price': '$60', 'quantity': 3},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history', 'ISBN': '1234567892', 'price': '$70', 'quantity': 2},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math', 'ISBN': '1234567893', 'price': '$80', 'quantity': 1},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math', 'ISBN': '1234567894', 'price': '$90', 'quantity': 4},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math', 'ISBN': '1234567895', 'price': '$100', 'quantity': 6}
]


@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book


@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(updated_book: dict = Body(...)):
    for i, book in enumerate(BOOKS):
        if book.get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book
            return {"message": "Book updated successfully."}
    return {"message": "Book not found."}


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            return {"message": f"Book '{book_title}' deleted successfully."}
    return {"message": f"Book '{book_title}' not found."}


# --- Assessment

@app.get('/Books/{author}/')
async def Fetch_all_books_from_specific_author(Author: str):
    books_from_author = []
    for book in Books:
        if book.get('Author').casefold() == Author.casefold():
            books_from_author.append(book)
    if len(books_from_author) == 0:
        return {"Message": f"No book with author '{Author}' found"}
    else:
        return books_from_author