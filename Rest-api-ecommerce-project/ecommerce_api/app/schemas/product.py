# app/schemas/product.py
from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    id: int

    class Config:
        orm_mode = True