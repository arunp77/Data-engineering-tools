from pydantic import BaseModel
from enum import Enum

class TestType(str, Enum):
    positioning_test = "Positioning test"
    validation_test = "Validation test"
    total_boot_camp = "Total Boot Camp"

class Question(BaseModel):
    question: str
    subject: str
    use: TestType
    correct: str
    responseA: str
    responseB: str
    responseC: str
    responseD: str
    remark: str
