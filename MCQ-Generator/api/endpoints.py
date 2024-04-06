from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import HTTPBasicCredentials
from typing import List
from api.models import Question, QuestionRequest, Token, QuestionCreate
from api.auth import authenticate_user
from api.utils import load_question_data
import random

router = APIRouter()


# Load question data from Excel file
questions_db = load_question_data("data/questions_en.xlsx")

@router.get("/questions/", response_model=List[Question], tags=["Questions"])
def get_questions(request: QuestionRequest):
    """
    Retrieve a list of questions based on the provided criteria.

    - **request**: A `QuestionRequest` object containing the test type, categories, and number of questions.
    - **returns**: A list of `Question` objects.
    """
    # Implementation logic to fetch questions from the database based on request
    # Mock implementation for demonstration
    if request.test_type == "Total Boot Camp":
        selected_questions = [q for q in questions_db if q.use == request.test_type and q.subject in request.categories]
    else:
        selected_questions = [q for q in questions_db if q.use == request.test_type]

    # Randomize and select questions based on num_questions
    if len(selected_questions) > request.num_questions:
        selected_questions = random.sample(selected_questions, request.num_questions)

    return selected_questions

@router.post("/token/", response_model=Token)
def login(credentials: HTTPBasicCredentials = Depends(authenticate_user)):
    # Generate JWT token for authentication
    # Implement your authentication logic here
    return {"access_token": "fake_token", "token_type": "bearer"}

@router.post("/questions/", status_code=status.HTTP_201_CREATED, tags=["Questions"])
def create_question(question: QuestionCreate, credentials: HTTPBasicCredentials = Depends(authenticate_user)):
    """
    Create a new question (for admin user only).

    - **question**: A `QuestionCreate` object containing the details of the new question.
    - **credentials**: HTTP Basic credentials for admin authentication.
    - **returns**: A message indicating the successful creation of the question.
    """
    # Create a new question in the database (for admin user only)
    # Implement your logic here to create a new question in the database
    questions_db.append(question)
    return {"message": "Question created successfully"}
