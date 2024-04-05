from pydantic import BaseModel

class Question(BaseModel):
    question: str
    subject: str
    use: str
    correct: str  
    responseA: str
    responseB: str
    responseC: str
    responseD: str = None
    remark: str = None
