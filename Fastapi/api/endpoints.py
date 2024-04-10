from fastapi import APIRouter, Depends
from fastapi.responses import Response, JSONResponse
import json
from typing import List
from fastapi import Query
from fastapi.security import HTTPBasic
from api.auth import authenticate
from api.models import TestType, Question, Subject
from api.utils import generate_questions

router = APIRouter()

@router.get("/verify")
def verify_api():
    return {"status": "API is functional"}

# @router.get("/generate_questions/")
# def generate_mcqs(
    # test_type: TestType,
    # categories: list[str],
    # num_questions: int,
    #username: str = Depends(authenticate)
# ):
    # questions = generate_questions(test_type, categories, num_questions)
    # return {"questions": questions}

# @router.get("/generate_questions/")
# def generate_mcqs(
#     test_type: TestType,
#     subject: Subject,
#     num_questions: int = Query(..., description="Select the number of questions"),
#     username: str = Depends(authenticate)
# ):
#     questions = generate_questions(test_type, subject, num_questions)
    
#     # Convert float values to strings or handle out-of-range values here if necessary
    
#     # Example: Convert float values to strings
#     for question in questions:
#         question["float_field"] = str(question["float_field"])
    
#     return {"questions": questions}

@router.get("/generate_questions/")
def generate_mcqs(
    test_type: TestType,
    subject: Subject = Query(..., description="Select one or more categories"),
    num_questions: int = Query(..., description="Select the number of questions"),
    username: str = Depends(authenticate)
):
    questions = generate_questions(test_type, [subject], num_questions)
    
    return {"questions": questions}