# Machine Learning Model Deployment with Flask API

## Overview
This project aims to deploy machine learning models using Flask APIs. Three different types of models are deployed:

1. **Structured Data Model**: A machine learning model trained on the Kaggle Titanic dataset to predict survival on the Titanic.
2. **NLP Model**: A natural language processing model (not provided in this README) for text classification.
3. **Image Classification Model**: An image classification model (not provided in this README).

## Project Structure
- **api.py**: Flask API script for handling model predictions.
- **svm_titanic.pkl**: Pickle file containing the trained SVM model for Titanic survival prediction.
- *(Other model files if applicable)*

## Usage
### Prerequisites
- Python 3.x
- Flask
- scikit-learn

### Running the API
1. **Clone the repository:** `git clone https://github.com/arunp77/Data-engineering-tools.git`
2. **Navigate to the project directory:** `cd FLask/Flask-machine-learning` which is inside the `Flask` folder of the home directory.
3. Install dependencies: `pip install -r requirements.txt`
4. Run the Flask API: `python api.py`

### Making Predictions
- Send a POST request to `http://localhost:5000/predict` with JSON data containing the features required for prediction.
- Example JSON data:
```json
{
    "pclass": 1,
    "sex": 1,
    "age": 32,
    "fare": 50,
    "embarked": 0,
    "single": 0,
    "famillySize": [0, 1, 0],
    "title": 2
}
```

## Endpoint Details
- **URL**: `/predict`
- **Method**: POST
- **Request Body**: JSON format with required features
- **Response**: JSON format with prediction result

## Feature Description
- **pclass**: Ticket class (1, 2, 3)
- **sex**: Passenger's sex (0 for male, 1 for female)
- **age**: Age class (0 for under 16, 1 for under 32, 2 for under 48, 3 for under 64, 4 for over 64)
- **fare**: Price class (0 for under $7.91, 1 for under $14.454, 2 for under $31, 3 for over $31)
- **embarked**: Port of embarkation (0 = Southampton, 1 = Cherbourg, 2 = Queenstown)
- **single**: Passenger embarked alone or accompanied (1 for alone, 0 for accompanied)
- **familySize**: Size of passenger's family (one-hot encoding)
- **title**: Passenger's title (1: Mr, 2: Miss, 3: Mrs, 4: Master, 5: Rare)

## Acknowledgments
- Kaggle Titanic Dataset: [Link](https://www.kaggle.com/c/titanic)
