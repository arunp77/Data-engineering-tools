"""
FastAPI Multiple Choice Questions (MCQs) Generator API

This FastAPI application provides a RESTful API for managing MCQs (Multiple Choice Questions). Users can perform the following actions:

* **Manage Questionnaires:** Create, retrieve, update, and delete questionnaires.
* **Authenticate Users:** Implement user authentication mechanisms (not explicitly shown in this code example).
* **Create Questions:** Create new questions for inclusion in questionnaires.

**Key Features:**

* **OpenAPI Documentation:** Generates interactive API documentation at `/docs` and `/redoc` for easy exploration and testing.
* **Custom Error Handling:** Provides two exception handlers:
    * `http_exception_handler`: Handles HTTPExceptions, returning a JSON response with the exception's status code and detail message.
    * `generic_exception_handler`: Catches any unhandled exceptions, returning a generic JSON response with a 500 Internal Server Error status code and a message indicating an internal server error.
* **User-Friendly:** Includes detailed API descriptions and versioning information.

**Created By:** Arun Kumar Pandey

**Version:** 1.0.0

**How to Run:**

1. **Install Dependencies:** Ensure you have FastAPI and Uvicorn installed (e.g., using `pip install fastapi uvicorn`).
2. **Start the Server:** Run the application from the command line using:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   
"""

from fastapi import FastAPI
from api.endpoints import router as api_router
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI(
    title="FastAPI Multiple Choice Questions (MCQs) Generator ",
    description="This API allows users to manage questionnaires, authenticate users, and create questions. This API is created by <strong>Arun Kumar Pandey</strong>.",
    version="1.0.0"
)

app.include_router(api_router)

# Define custom error handler middleware
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )

@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    # Handle generic exceptions
    return JSONResponse(
        status_code=500,
        content={"message": "Internal server error"}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)