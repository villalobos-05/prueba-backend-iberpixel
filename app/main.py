from fastapi import FastAPI
from .routers import localBooks

app = FastAPI()
app.include_router(localBooks.router)
