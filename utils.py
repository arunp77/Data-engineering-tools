import pandas as pd
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

def load_questions(excel_file):
    df = pd.read_excel(excel_file)
    # ... data cleaning and processing if needed
    return df


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "arunp77"  # Replace with a secure key
ALGORITHM = "HS256"

users_db = {
  "alice": pwd_context.hash("wonderland"),
  "bob": pwd_context.hash("builder"),
  "clementine": pwd_context.hash("mandarine"),
  "admin": pwd_context.hash("4dm1N")
}

def get_users_db():
    return users_db

# ... authentication functions (get_user, verify_password, create_token) 
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user(db, username: str):
    if username in db:
        return {"username": username}

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)  # Default expiration
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

