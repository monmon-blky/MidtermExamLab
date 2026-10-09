from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from models import Category, Book


def create_category(db: Session, data):
    category = Category(**data.model_dump())
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def get_categories(db: Session):
    return db.query(Category).order_by(Category.id).all()


def create_book(db: Session, data):
    if db.get(Category, data.category_id) is None:
        raise HTTPException(status_code=400, detail="Category does not exist")

    book = Book(**data.model_dump())
    db.add(book)
    try:
        db.commit()
        db.refresh(book)
        return book
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="ISBN already exists")


def get_books(db: Session, category_id: int | None = None):
    query = db.query(Book)
    if category_id is not None:
        if db.get(Category, category_id) is None:
            raise HTTPException(status_code=404, detail="Category not found")
        query = query.filter(Book.category_id == category_id)
    return query.order_by(Book.id).all()


def get_book(db: Session, book_id: int):
    book = db.get(Book, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


def update_book(db: Session, book_id: int, data):
    book = get_book(db, book_id)
    updates = data.model_dump(exclude_unset=True)

    if "category_id" in updates:
        if updates["category_id"] is None:
            raise HTTPException(status_code=400, detail="Category ID cannot be null")
        if db.get(Category, updates["category_id"]) is None:
            raise HTTPException(status_code=400, detail="Category does not exist")

    for key, value in updates.items():
        if value is None and key in {"title", "isbn", "stock_quantity", "category_id"}:
            raise HTTPException(status_code=400, detail=f"{key} cannot be null")
        setattr(book, key, value)

    try:
        db.commit()
        db.refresh(book)
        return book
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="ISBN already exists")


def delete_book(db: Session, book_id: int):
    book = get_book(db, book_id)
    db.delete(book)
    db.commit()
