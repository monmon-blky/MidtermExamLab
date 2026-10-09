CS 315a Cloud Computing - Library Book Inventory API

FILES
- main.py: FastAPI app and endpoints
- database.py: SQLite connection and database session
- models.py: SQLAlchemy Category and Book models
- schemas.py: Pydantic request/response validation
- crud.py: database operations and error handling
- requirements.txt: Python dependencies

RUN ON REPLIT
1. Upload/extract this project into a Python Repl so the .py files are at the project root.
2. In the Shell, run:
   python -m pip install -r requirements.txt
3. Run:
   python -m uvicorn main:app --host 0.0.0.0 --port 8000
4. Open the Replit web preview, or open your app URL and add /docs.

TESTING ORDER
1. POST /categories/
   {"name":"Programming","description":"Programming books"}
2. POST /books/
   {"title":"Python Basics","isbn":"9781234567890","publication_year":2025,"stock_quantity":10,"category_id":1}
3. Test GET /categories/, GET /books/, GET /books/?category_id=1,
   GET /books/1, PUT /books/1, and DELETE /books/1.

NOTES
- New category/book: HTTP 201.
- Successful reads/updates/deletes: HTTP 200.
- Missing book/category during lookup: HTTP 404.
- Duplicate ISBN or invalid category when creating/updating a book: HTTP 400.
- SQLite database file library.db is created automatically.
