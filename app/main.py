from fastapi import FastAPI, HTTPException, status
from app.models.book import Book, CreateBook, UpdateBook
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


@app.post("/api/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: CreateBook):
    new_book = InMemoryBook(book)
    BOOKS.append(new_book)
    return new_book


@app.put("/api/books/{id}", response_model=Book)
def update_book(id: int, newBook: UpdateBook):
    index = next((i for i, b in enumerate(BOOKS) if b["id"] == id), None)

    if index is None:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail=f"Book with id {id} not found"
        )

    BOOKS[index].update(newBook.model_dump(exclude_unset=True))

    return BOOKS[index]


@app.patch("/api/books/{id}/read", response_model=Book)
def toggle_book_read_status(id: int):
    index = next((i for i, b in enumerate(BOOKS) if b["id"] == id), None)

    if index is None:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail=f"Book with id {id} not found"
        )

    BOOKS[index]["isRead"] = not BOOKS[index]["isRead"]
    return BOOKS[index]
