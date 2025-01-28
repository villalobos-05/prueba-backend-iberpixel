from fastapi import FastAPI
from .routers import localBooks, books

app = FastAPI()
app.include_router(localBooks.router)
app.include_router(books.router)
