from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from .models import UserCredentials

security = HTTPBasic()

# Dictionary to store user credentials
users = {
    "alice": "wonderland",
    "bob": "builder",
    "clementine": "mandarine",
    "admin": "4dm1N"  # Admin user for creating questions
}

def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    # Implementation of authentication logic
    # Verify user credentials
    if credentials.username not in users or users[credentials.username] != credentials.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic realm='Authentication required'"},
        )
    return UserCredentials(username=credentials.username, password=credentials.password)

def authorize_admin(user: UserCredentials = Depends(authenticate_user)):
    # Implementation of authorization logic
    # Allow access for admin user only
    if user.username != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to perform this action",
        )
    return user
