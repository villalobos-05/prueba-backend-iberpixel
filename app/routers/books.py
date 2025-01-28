from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Depends
from app.models.book import Book, CreateBook, UpdateBook
from app.schemas.book import book_schema, books_schema
from app.utils.getActualDatetime import getActualDatetime
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
        raiseBookNotFoundById(id)

    return book_schema(book)


@router.post("/books", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_book(book: CreateBook):
    response = await collection.insert_one(
        {**book.model_dump(), "createdAt": getActualDatetime()}
    )
    createdBook = await collection.find_one({"_id": response.inserted_id})

    return book_schema(createdBook)


@router.put("/books/{id}", response_model=Book)
async def update_book(id: Annotated[str, Depends(getObjectId)], newBook: UpdateBook):
    book = await collection.find_one_and_update(
        {"_id": id},
        {"$set": newBook.model_dump(exclude_unset=True)},
        return_document=True,
    )

    if not book:
        raiseBookNotFoundById(id)

    return book_schema(book)


@router.patch("/books/{id}/read", response_model=Book)
async def toggle_book_read_status(id: Annotated[str, Depends(getObjectId)]):
    book = await collection.find_one({"_id": id})

    if not book:
        raiseBookNotFoundById(id)

    updatedBook = await collection.find_one_and_update(
        {"_id": id},
        {"$set": {"isRead": not book["isRead"]}},
        return_document=True,
    )

    return book_schema(updatedBook)


# Just not to write the same exception over and over again
def raiseBookNotFoundById(id: str):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {id} not found"
    )
