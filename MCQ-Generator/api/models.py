from pydantic import BaseModel
from typing import List, Optional

class Question(BaseModel):
    question: str
    subject: str
    use: str
    correct: str
    responseA: str
    responseB: str
    responseC: Optional[str] = None
    responseD: Optional[str] = None

class QuestionRequest(BaseModel):
    test_type: str
    categories: List[str]
    num_questions: int

class UserCredentials(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class QuestionCreate(BaseModel):
    question: str
    subject: str
    use: str
    correct: str
    responseA: str
    responseB: str
    responseC: Optional[str] = None
    responseD: Optional[str] = None
