from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from fastapi import HTTPException, Depends, status

security = HTTPBasic()

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    """
    Authenticates the user based on provided credentials.

    Parameters:
    - credentials (HTTPBasicCredentials): The username and password provided in the request.

    Returns:
    - Tuple[str, bool]: A tuple containing the username and a boolean indicating whether the user is a superuser.

    Raises:
    - HTTPException: If the provided username or password is incorrect.
    """
    correct_username = credentials.username
    correct_passwords = {
        "alice": "wonderland",
        "bob": "builder",
        "clementine": "mandarine",
        "admin": "4dm1N"
    }
    
    correct_password = correct_passwords.get(correct_username)
    
    if correct_username == "admin" and credentials.password == correct_password:
        return correct_username, True
    elif not correct_password or credentials.password != correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    else:
        return correct_username, False

class Token(BaseModel):
    """
    Model representing an access token.

    Attributes:
    - access_token (str): The access token string.
    - token_type (str): The type of token.
    """
    access_token: str
    token_type: str
