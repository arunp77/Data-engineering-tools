from fastapi import FastAPI
from api.endpoints import router as api_router
from api.auth import router as api_router

app = FastAPI(
    title="Questionnaire API",
    description="This API allows users to manage questionnaires, authenticate users, and create questions.",
    version="1.0.0"
)

app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)