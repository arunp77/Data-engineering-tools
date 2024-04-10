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