# api/utils.py
import pandas as pd

def load_question_data(file_path):
    """
    Load question data from an Excel file.
    """
    try:
        df = pd.read_excel(file_path)
        questions = df.to_dict(orient='records')
        return questions
    except Exception as e:
        raise ValueError(f"Error loading question data: {str(e)}")


def process_question_data(data):
    """
    Process question data before returning to the client.
    This could include formatting, filtering, or any other data manipulation.
    """
    # Implement your logic here
    return data

def validate_question_data(question):
    """
    Validate question data before creating a new question.
    This could include checking for required fields, data types, etc.
    """
    # Implement your validation logic here
    if not question.get('question'):
        raise ValueError("Question title is required")
    # Additional validation checks...

def handle_error(error):
    """
    Handle errors gracefully and return appropriate responses.
    """
    # Log the error
    print(f"An error occurred: {error}")
    # Return appropriate error response
    return {"error": str(error)}
