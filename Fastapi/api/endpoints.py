from fastapi import APIRouter, Depends
from fastapi.responses import Response, JSONResponse
import json
from typing import List
from fastapi import Query
from fastapi.security import HTTPBasic
from fastapi.security import HTTPBasicCredentials
from api.auth import authenticate
from api.models import TestType, Question, Subject
from api.utils import generate_questions


router = APIRouter()

@router.get("/verify", name="Status", description="Root endpoint to verify the success of the API creation.")
def verify_api():
    """
    Verifies the functionality of the API.

    Returns:
        dict: A JSON object indicating the status of the API.
    """
    return {"status": "API is functional"}


@router.get("/generate_questions/")
def generate_mcqs(
    test_type: TestType,
    subject: Subject = Query(..., description="Select one or more categories"),
    num_questions: int = Query(..., description="Select the number of questions"),
    username: str = Depends(authenticate)
):
    """
    **Generates the questions:** Generates multiple-choice questions based on specified parameters.

    **Args:**
        test_type (TestType): The type of test for which questions are generated.
        subject (Subject): The subject/category for the questions.
        num_questions (int): The number of questions to generate.
        username (str, optional): The username for authentication. Defaults to None.

    **Returns:**
        dict: A JSON object containing the generated questions.
    """
    questions = generate_questions(test_type, [subject], num_questions)
    
    return {"questions": questions}