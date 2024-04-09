from fastapi import APIRouter, Depends
from .auth import authenticate
from .models import TestType, Question
from .utils import generate_questions

router = APIRouter()

@router.get("/verify")
def verify_api():
    return {"status": "API is functional"}

@router.get("/generate_questions/")
def generate_mcqs(
    test_type: TestType,
    categories: list[str],
    num_questions: int,
    username: str = Depends(authenticate)
):
    questions = generate_questions(test_type, categories, num_questions)
    return {"questions": questions}
