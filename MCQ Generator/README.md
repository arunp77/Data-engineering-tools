# Project Title: FastAPI MCQ Generator with Authentication and Admin Features

[Project Github repository](https://github.com/arunp77/FastApi-userdatabase/tree/main/MCQ%20Generator)

## Overview:
This project aims to create a FastAPI application to generate Multiple Choice Questions (MCQs) via a smartphone or web browser application. The API allows users to select test types, categories, and the number of questions to receive randomized MCQs. Additionally, the API supports basic authentication for user verification and admin features for question management.

## Project directory structure

```bash
project_folder/
│
├── api/
│   ├── __init__.py
│   ├── auth.py
│   ├── endpoints.py
│   ├── models.py
│   └── utils.py
│
├── data/
│   └── questions_en.xlsx
│
├── tests/
│   └── test_api.py
│
├── main.py
└── requirements.txt
```

## Features:
1. **Question Generation**: Users can request MCQs based on test type and categories, with the option to specify the number of questions. Questions are returned in a random order.
   
2. **User Authentication**: Basic authentication is implemented to verify user credentials. Users must provide a valid username and password to access the API endpoints.
   
3. **Admin Features**: Admin users with the password "4dm1N" can create new questions via a dedicated endpoint. This ensures seamless management of the question database.

## Endpoints:
- `/generate_questions`: POST endpoint to generate MCQs based on test type, categories, and the number of questions requested.
- `/authenticate`: POST endpoint for user authentication. Users must provide valid credentials to access protected endpoints.
- `/create_question`: POST endpoint for admin users to create new questions. Requires admin credentials for authorization.

## Setup:
1. **Clone the repository from GitHub:** `git clone https://github.com/arunp77/FastApi-userdatabase.git`
2. **Install dependencies from requirements.txt:** `pip install -r requirements.txt`
3. **Run the FastAPI application:** `uvicorn main:app --reload`

## Usage:
1. Generate MCQs:
   - Send a POST request to `/generate_questions` with the following parameters:
     - `use`: Test type (e.g., "Positioning test", "Validation test", "Total Boot Camp")
     - `categories`: List of categories (e.g., "Databases", "Machine Learning")
     - `num_questions`: Number of questions to generate
   - Include authentication credentials in the request headers (`Authorization: Basic <username:password>`).
2. Authenticate User:
   - Send a POST request to `/authenticate` with the following parameters:
     - `username`: User's username
     - `password`: User's password
3. Create New Question (Admin Only):
   - Send a POST request to `/create_question` with the new question details.
   - Include admin credentials in the request headers (`Authorization: Basic admin:4dm1N`).

## Testing:
- Detailed instructions for testing the API can be found in the provided test_commands.txt file.

## Architecture Choices:
- FastAPI chosen for its simplicity, performance, and automatic interactive documentation.
- Pandas utilized for efficient data manipulation and handling of the question dataset.
- Basic authentication implemented for user verification, with credentials securely passed in the request headers.
- Endpoints designed to be intuitive and RESTful for ease of use.
- Python's random module used for shuffling questions to ensure randomization.

## Contributing:
Contributions to the project are welcome! Please fork the repository, make your changes, and submit a pull request with a detailed description of the proposed changes.

## License:
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements:
- Special thanks to the FastAPI community for their excellent documentation and support.
- Thanks to the contributors who have helped improve this project.

## Contact:
For inquiries or feedback, please contact [arunp77@gmail.com](mailto:arunp77@gmail.com).

## References:
- FastAPI Documentation: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
- Pandas Documentation: [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)

## Author:
[Arun Kumar Pandey] - [GitHub Profile](https://github.com/arunp77)