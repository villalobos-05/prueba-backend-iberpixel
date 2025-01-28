from app.models.book import Book


def book_schema(book) -> Book:
    return Book(
        id=str(book["_id"]),
        title=book["title"],
        author=book["author"],
        isRead=book["isRead"],
        createdAt=book["createdAt"],
    )


def books_schema(books) -> list[Book]:
    return [book_schema(book) for book in books]
