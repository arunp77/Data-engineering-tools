from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Dummy database of questions
class QuestionDB:
    def __init__(self):
        self.questions = [
            {"id": 1, "text": "What is your favorite color?"},
            {"id": 2, "text": "What is the capital of France?"},
            {"id": 3, "text": "What is the square root of 64?"}
        ]
    
    def get_questions(self) -> List[dict]:
        return self.questions

app = FastAPI()


# Initialize database
question_db = QuestionDB()

# Define request model
class QuestionRequest(BaseModel):
    pass

# Define response model
class QuestionResponse(BaseModel):
    id: int
    text: str


@app.get("/")
async def root():
    return {"message": "Welcome to the question API!"}

# API route to get questions
@app.get("/questions/", response_model=List[QuestionResponse])
async def get_questions():
    questions = question_db.get_questions()
    return questions
