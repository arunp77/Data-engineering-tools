from fastapi import FastAPI
from app.routers import auth, payments, products  # Ensure these imports are correct
from pydantic import BaseSettings

app = FastAPI()

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(payments.router, prefix="/payments", tags=["payments"])
app.include_router(products.router, prefix="/products", tags=["products"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Ecommerce API!"} 
