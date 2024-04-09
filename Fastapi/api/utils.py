import pandas as pd
import random

def load_questions(file_path):
    return pd.read_excel(file_path)

def filter_questions(df, test_type, categories):
    return df[(df['use'] == test_type) & (df['subject'].isin(categories))]

def select_random_questions(questions, num_questions):
    return random.sample(questions.to_dict(orient='records'), num_questions)

def generate_questions(test_type, categories, num_questions, file_path='data/questions_en.xlsx'):
    df = load_questions(file_path)
    filtered_questions = filter_questions(df, test_type, categories)
    selected_questions = select_random_questions(filtered_questions, num_questions)
    return selected_questions
