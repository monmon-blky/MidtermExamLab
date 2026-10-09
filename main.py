from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from schemas import (
    CategoryCreate,
    CategoryResponse,
    BookCreate,
    BookUpdate,
    BookResponse,
)
from crud import (
    create_category,
    get_categories,
    create_book,
    get_books,
    get_book,
    update_book,
    delete_book,
)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Library Book Inventory API")


@app.get("/")
def home():
    return {"message": "Library Book Inventory API is running", "docs": "/docs"}


@app.post(
    "/categories/",
    response_model=CategoryResponse,
    status_code=201,
)
def add_category(data: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, data)


@app.get("/categories/", response_model=list[CategoryResponse])
def list_categories(db: Session = Depends(get_db)):
    return get_categories(db)


@app.post("/books/", response_model=BookResponse, status_code=201)
def add_book(data: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, data)


@app.get("/books/", response_model=list[BookResponse])
def list_books(
    category_id: int | None = None,
    db: Session = Depends(get_db),
):
    return get_books(db, category_id)


@app.get("/books/{book_id}", response_model=BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    return get_book(db, book_id)


@app.put("/books/{book_id}", response_model=BookResponse)
def edit_book(
    book_id: int,
    data: BookUpdate,
    db: Session = Depends(get_db),
):
    return update_book(db, book_id, data)


@app.delete("/books/{book_id}")
def remove_book(book_id: int, db: Session = Depends(get_db)):
    delete_book(db, book_id)
    return {"message": "Book deleted successfully"}
