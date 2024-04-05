from fastapi import FastAPI, Query
from typing import List, Optional
import pandas as pd
import random

# Load the dataset
df = pd.read_excel("questions_en.xlsx")

# Initialize FastAPI
app = FastAPI()

# Define endpoint to get questions
@app.get("/questions/")
async def get_questions(
    test_type: Optional[str] = None,
    categories: Optional[List[str]] = Query(None),
    num_questions: Optional[int] = 5):
    # Filter questions based on test type and categories
    if test_type:
        filtered_df = df[df['use'] == test_type]
    else:
        filtered_df = df
    
    if categories:
        filtered_df = filtered_df[filtered_df['subject'].isin(categories)]

    # Shuffle the DataFrame to return questions in random order
    shuffled_df = filtered_df.sample(frac=1).reset_index(drop=True)

    # Select the required number of questions
    selected_questions = shuffled_df.head(num_questions)

    # Convert selected questions to JSON format
    questions_json = selected_questions.to_dict(orient='records')

    return questions_json