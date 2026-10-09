from pydantic import BaseModel, ConfigDict, Field


class CategoryCreate(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    description: str | None = None


class CategoryResponse(BaseModel):
    id: int
    name: str
    description: str | None

    model_config = ConfigDict(from_attributes=True)


class BookCreate(BaseModel):
    title: str = Field(min_length=1, max_length=300)
    isbn: str = Field(min_length=1, max_length=50)
    publication_year: int | None = None
    stock_quantity: int = Field(default=1, ge=0)
    category_id: int = Field(gt=0)


class BookUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=300)
    isbn: str | None = Field(default=None, min_length=1, max_length=50)
    publication_year: int | None = None
    stock_quantity: int | None = Field(default=None, ge=0)
    category_id: int | None = Field(default=None, gt=0)


class BookResponse(BaseModel):
    id: int
    title: str
    isbn: str
    publication_year: int | None
    stock_quantity: int
    category_id: int

    model_config = ConfigDict(from_attributes=True)
