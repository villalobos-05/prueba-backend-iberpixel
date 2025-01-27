from fastapi import APIRouter, HTTPException, status
from app.models.book import Book, CreateBook, UpdateBook
from app.utils.getActualDatetime import getActualDatetime

router = APIRouter(
    prefix="/api/local",
    tags=["local books (only books stored in local memory)"],
)


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


@router.get("/books", response_model=list[Book])
def get_books(author: str | None = None, title: str | None = None):
    filtered_books = BOOKS

    if author:
        filtered_books = [
            book for book in filtered_books if book["author"].lower() == author.lower()
        ]

    if title:
        filtered_books = [
            book for book in filtered_books if book["title"].lower() == title.lower()
        ]

    return filtered_books


@router.get("/books/{id}", response_model=Book)
def get_book_by_id(id: int):
    bookFound = next((book for book in BOOKS if book["id"] == id), None)

    if not bookFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {id} not found"
        )

    return bookFound


@router.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: CreateBook):
    new_book = InMemoryBook(book)
    BOOKS.routerend(new_book)
    return new_book


@router.put("/books/{id}", response_model=Book)
def update_book(id: int, newBook: UpdateBook):
    index = next((i for i, b in enumerate(BOOKS) if b["id"] == id), None)

    if index is None:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail=f"Book with id {id} not found"
        )

    BOOKS[index].update(newBook.model_dump(exclude_unset=True))

    return BOOKS[index]


@router.patch("/books/{id}/read", response_model=Book)
def toggle_book_read_status(id: int):
    index = next((i for i, b in enumerate(BOOKS) if b["id"] == id), None)

    if index is None:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail=f"Book with id {id} not found"
        )

    BOOKS[index]["isRead"] = not BOOKS[index]["isRead"]
    return BOOKS[index]
