from fastapi import APIRouter, Depends
from fastapi.responses import Response, JSONResponse
import json
from typing import List
from fastapi import Query
from fastapi.security import HTTPBasic
from fastapi.security import HTTPBasicCredentials
from fastapi import HTTPException, Depends, status
from api.auth import authenticate
from api.models import TestType, Question, Subject
from api.utils import generate_questions
from typing import Dict


router = APIRouter()

@router.get("/verify", name="Status")
def verify_api():
    """
    Verifies the functionality of the API.

    **Returns:**
        <ul>
            <li><strong>dict:</strong> A JSON object indicating the status of the API.</li>
        </ul>
    """
    return {"status": "API is functional"}


@router.get("/generate_questions/", name="Generate Questions")
def generate_mcqs(
    test_type: TestType,
    subject: Subject = Query(..., description="Select one or more categories"),
    num_questions: int = Query(..., description="Select the number of questions"),
    username: str = Depends(authenticate)
):
    """
    **Generates the questions:** Generates multiple-choice questions based on specified parameters.

    **Args:**
        <ul>
            <li><code>test_type </code> (TestType): The type of test for which questions are generated.</li>
            <li><code>subject </code>(Subject): The subject/category for the questions.</li>
            <li><code>num_questions </code>(int): The number of questions to generate.</li>
            <li><code>username </code>(str, optional): The username for authentication. Defaults to None.</li>
        </ul>

    **Returns:**
        <ul>
            <li><strong>dict:</strong> A JSON object containing the generated questions.</li>
        </ul>
    """
    questions = generate_questions(test_type, [subject], num_questions)
    
    return {"questions": questions}

@router.post("/create_question", name="Create Question")
def create_question(
    question_data: Question,
    credentials: tuple = Depends(authenticate)
) -> Dict[str, str]:
    """
    Create a new question.

    Args:
        - question_data (Question): The data for the new question.
        - credentials (tuple): The result of the authentication, containing the username and a boolean indicating if the user is a superuser.

    Returns:
        - dict: A JSON object containing a message confirming the creation of the question.
    """
    # Check if the user is a superuser
    username, is_superuser = credentials
    if not is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only superusers can create questions",
        )

    # Here you would typically save the question data to your database or perform any necessary processing
    # For demonstration purposes, let's just return the received data as confirmation
    return {"message": "Question created successfully", "question_data": question_data.dict()}