from fastapi import APIRouter
from app.models.book import Book
from app.schemas.book import books_schema
from app.database import get_database

router = APIRouter(
    prefix="/api",
    tags=["books (mongodb)"],
)

client = get_database()
collection = client["books"]


@router.get("/books", response_model=list[Book])
async def get_books(author: str | None = None, title: str | None = None):
    query = {}

    if author:
        query["author"] = author
    if title:
        query["title"] = title

    books = await collection.find(query).to_list()
    return books_schema(books)
