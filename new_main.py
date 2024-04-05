from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
import pandas as pd
import random
import base64

# Load the dataset
df = pd.read_excel("questions_en.xlsx")

# User credentials dictionary
credentials = {
    "alice": "wonderland",
    "bob": "builder",
    "clementine": "mandarine"
}

# Define models
class User(BaseModel):
    username: str
    password: str

class Question(BaseModel):
    question: str
    subject: str
    use: str
    correct: str
    responseA: str
    responseB: str
    responseC: str
    responseD: Optional[str] = None
    remark: Optional[str] = None

# FastAPI app
app = FastAPI()

# Authentication function
def authenticate_user(credentials: User):
    encoded_credentials = base64.b64encode(f"{credentials.username}:{credentials.password}".encode("utf-8"))
    if encoded_credentials.decode("utf-8") not in [base64.b64encode(f"{u}:{p}".encode("utf-8")).decode("utf-8") for u, p in credentials.items()]:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return True

# Endpoint to generate questions
@app.post("/generate_questions")
def generate_questions(use: str, categories: List[str], num_questions: int, credentials: User = Depends(authenticate_user)):
    filtered_df = df[(df['use'] == use) & (df['subject'].isin(categories))]
    if len(filtered_df) < num_questions:
        raise HTTPException(status_code=400, detail="Insufficient questions available")
    questions = random.sample(filtered_df.to_dict(orient='records'), num_questions)
    return questions

# Endpoint for user authentication
@app.post("/authenticate")
def authenticate(credentials: User):
    return {"message": "Authentication successful"}

# Endpoint for admin to create new question
@app.post("/create_question")
def create_question(question: Question, credentials: User = Depends(authenticate_user)):
    if credentials.username != "admin" or credentials.password != "4dm1N":
        raise HTTPException(status_code=403, detail="Unauthorized")
    # Add the new question to the dataset (not implemented in this example)
    return {"message": "Question created successfully"}

# Endpoint to verify API functionality
@app.get("/healthcheck")
def healthcheck():
    return {"status": "API is up and running"}

# Testing command
# curl -X POST "http://localhost:8000/generate_questions" -H "Authorization: Basic YWxpY2U6d29uZGVybGFuZA==" -H "Content-Type: application/json" -d "{\"use\":\"Positioning test\",\"categories\":[\"Databases\",\"Data Streaming\"],\"num_questions\":5}"

