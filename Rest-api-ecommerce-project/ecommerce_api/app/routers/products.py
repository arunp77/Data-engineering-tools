# app/routers/products.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas import product as schemas
from app.models import product as models
from app.db.session import SessionLocal

from app.schemas.product import ProductCreate, ProductRead


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.ProductRead)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/", response_model=List[schemas.ProductRead])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products = db.query(models.Product).offset(skip).limit(limit).all()
    return products

# Add more endpoints for update, delete, etc.
# Define your routes here, for example:
@router.post("/products/", response_model=ProductRead)
def create_product(product: ProductCreate):
    # Implementation for creating a product
    pass