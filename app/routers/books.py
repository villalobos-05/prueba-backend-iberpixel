from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Depends
from app.models.book import Book
from app.schemas.book import book_schema, books_schema
from app.utils.getObjectId import getObjectId
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


@router.get("/books/{id}", response_model=Book)
async def get_book_by_id(id: Annotated[str, Depends(getObjectId)]):
    book = await collection.find_one({"_id": id})

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {id} not found"
        )

    return book_schema(book)
