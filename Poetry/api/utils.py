import pandas as pd
import random

def load_questions(file_path):
    """
    Load questions from an Excel file.

    Parameters:
    - file_path (str): Path to the Excel file containing the questions.

    Returns:
    - DataFrame: DataFrame containing the loaded questions.
    """
    return pd.read_excel(file_path)

# def filter_questions(df, test_type, categories):
#     return df[(df['use'] == test_type) & (df['subject'].isin(categories))]

def filter_questions(df, test_type, categories):
    """
    Filter questions based on test type and categories.

    Parameters:
    - df (DataFrame): DataFrame containing the questions.
    - test_type (TestType): Type of test to filter questions for.
    - categories (list): List of categories (Subject) to filter questions for.

    Returns:
    - DataFrame: Filtered DataFrame containing the questions.
    """
    categories_list = [cat.value for cat in categories]  # Convert enum values to a list
    return df[(df['use'] == test_type) & (df['subject'].isin(categories_list))]

def select_random_questions(questions, num_questions):
    """
    Select random questions from a DataFrame.

    Parameters:
    - questions (DataFrame): DataFrame containing the questions.
    - num_questions (int): Number of questions to select.

    Returns:
    - list: List of randomly selected questions as dictionaries.
    """
    return random.sample(questions.to_dict(orient='records'), num_questions)

# def generate_questions(test_type, categories, num_questions, file_path='data/questions_en.xlsx'):
#     df = load_questions(file_path)
#     filtered_questions = filter_questions(df, test_type, categories)
#     selected_questions = select_random_questions(filtered_questions, num_questions)
#     return selected_questions

def generate_questions(test_type, categories, num_questions, file_path='data/questions_en.xlsx'):
    """
    Generate random questions based on test type and categories.

    Parameters:
    - test_type (TestType): Type of test for the questions.
    - categories (list): List of categories (Subject) for the questions.
    - num_questions (int): Number of questions to generate.
    - file_path (str): Path to the Excel file containing the questions.

    Returns:
    - list: List of randomly generated questions as dictionaries.
    """
    df = load_questions(file_path)
    filtered_questions = filter_questions(df, test_type, categories)
    selected_questions = select_random_questions(filtered_questions, num_questions)

    # Convert any float values to strings
    for question in selected_questions:
        for key, value in question.items():
            if isinstance(value, float):
                question[key] = str(value)

    return selected_questions
