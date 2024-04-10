from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel

security = HTTPBasic()

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = credentials.username
    correct_password = {
        "alice": "wonderland",
        "bob": "builder",
        "clementine": "mandarine",
        "admin": "4dm1N"
    }.get(correct_username)
    
    if not correct_password or credentials.password != correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return correct_username

class Token(BaseModel):
    access_token: str
    token_type: str