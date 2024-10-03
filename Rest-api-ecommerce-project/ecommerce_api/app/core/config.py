# app/core/config.py
from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

class Settings(BaseSettings):
    SECRET_KEY: str
    STRIPE_SECRET_KEY: str
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()
