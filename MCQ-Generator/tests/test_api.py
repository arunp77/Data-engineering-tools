import random
from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBasicCredentials
from typing import List
from api.models import Question, QuestionRequest
from api.endpoints import router, questions_db  # Adjusted import path

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

    # Shuffle the list of selected questions
    random.shuffle(selected_questions)

    return selected_questions
