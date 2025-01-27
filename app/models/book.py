from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    author: str
    isRead: bool
    createdAt: str


class CreateBook(BaseModel):
    title: str
    author: str
    isRead: bool


class UpdateBook(BaseModel):
    title: str | None = None
    author: str | None = None
    isRead: bool | None = None
