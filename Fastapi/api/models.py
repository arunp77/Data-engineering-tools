from pydantic import BaseModel
from enum import Enum

class TestType(str, Enum):
    """
    Enumeration representing different types of tests.
    """
    positioning_test = "Positioning test"
    validation_test = "Validation test"
    total_boot_camp = "Total Boot Camp"

class Subject(str, Enum):
    """
    Enumeration representing different subjects.
    """
    databases = "Databases"
    distributed_systems = "Distributed systems"
    data_streaming = "Data Streaming"
    docker = "Docker"
    classification = "Classification"
    data_science = "Data Science"
    machine_learning = "Machine Learning"
    automation = "Automation"

class Question(BaseModel):
    """
    Model representing a multiple-choice question.

    Attributes:
    - question (str): The question text.
    - subject (Subject): The subject category of the question.
    - use (TestType): The type of test the question belongs to.
    - correct (str): The correct answer option.
    - responseA (str): Option A of the multiple-choice question.
    - responseB (str): Option B of the multiple-choice question.
    - responseC (str): Option C of the multiple-choice question.
    - responseD (str): Option D of the multiple-choice question.
    - remark (str): Additional remarks for the question.
    """
    question: str
    subject: Subject
    use: TestType
    correct: str
    responseA: str
    responseB: str
    responseC: str
    responseD: str
    remark: str
