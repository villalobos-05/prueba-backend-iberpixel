from fastapi import FastAPI, HTTPException, status
from app.models.book import Book, CreateBook
from app.utils.getActualDatetime import getActualDatetime

app = FastAPI()


# Just to count in memory book creations
class InMemoryBook:
    id_counter = 3  # Static id counter

    def __init__(self, book: CreateBook):
        self.id = InMemoryBook.id_counter
        self.title = book.title
        self.author = book.author
        self.isRead = book.isRead
        self.createdAt = getActualDatetime()

        # Increase id counter for the next book created
        InMemoryBook.id_counter += 1


# Database in memory
BOOKS: list[Book] = [
    {
        "id": 1,
        "title": "Don Quijote",
        "author": "Miguel de Cervantes",
        "isRead": False,
        "createdAt": "2024-01-22T10:00:00Z",
    },
    {
        "id": 2,
        "title": "Luces de bohemia",
        "author": "Valle-Inclán",
        "isRead": True,
        "createdAt": "2024-06-24T12:00:00Z",
    },
]


@app.get("/api/books", response_model=list[Book])
def get_books():
    return BOOKS


@app.get("/api/books/{id}", response_model=Book)
def get_book_by_id(id: int):
    bookFound = next((book for book in BOOKS if book["id"] == id), None)

    if not bookFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {id} not found"
        )

    return bookFound


@app.post("/api/books", response_model=Book)
def create_book(book: CreateBook):
    new_book = InMemoryBook(book)
    BOOKS.append(new_book)
    return new_book
