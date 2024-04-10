from pydantic import BaseModel
from enum import Enum

class TestType(str, Enum):
    positioning_test = "Positioning test"
    validation_test = "Validation test"
    total_boot_camp = "Total Boot Camp"

class Subject(str, Enum):
    databases = "Databases"
    distributed_systems = "Distributed systems"
    data_streaming = "Data Streaming"
    docker = "Docker"
    classification = "Classification"
    data_science = "Data Science"
    machine_learning = "Machine Learning"
    automation = "Automation"

class Question(BaseModel):
    question: str
    subject: Subject
    use: TestType
    correct: str
    responseA: str
    responseB: str
    responseC: str
    responseD: str
    remark: str
