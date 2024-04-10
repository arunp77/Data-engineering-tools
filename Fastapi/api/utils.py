import pandas as pd
import random

def load_questions(file_path):
    return pd.read_excel(file_path)

# def filter_questions(df, test_type, categories):
#     return df[(df['use'] == test_type) & (df['subject'].isin(categories))]

def filter_questions(df, test_type, categories):
    categories_list = [cat.value for cat in categories]  # Convert enum values to a list
    return df[(df['use'] == test_type) & (df['subject'].isin(categories_list))]

def select_random_questions(questions, num_questions):
    return random.sample(questions.to_dict(orient='records'), num_questions)

# def generate_questions(test_type, categories, num_questions, file_path='data/questions_en.xlsx'):
#     df = load_questions(file_path)
#     filtered_questions = filter_questions(df, test_type, categories)
#     selected_questions = select_random_questions(filtered_questions, num_questions)
#     return selected_questions

def generate_questions(test_type, categories, num_questions, file_path='data/questions_en.xlsx'):
    df = load_questions(file_path)
    filtered_questions = filter_questions(df, test_type, categories)
    selected_questions = select_random_questions(filtered_questions, num_questions)

    # Convert any float values to strings
    for question in selected_questions:
        for key, value in question.items():
            if isinstance(value, float):
                question[key] = str(value)

    return selected_questions