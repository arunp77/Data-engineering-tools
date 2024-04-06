from fastapi import FastAPI
from api.endpoints import router as api_router

app = FastAPI(
    title="Questionnaire API",
    description="This API allows users to manage questionnaires, authenticate users, and create questions.",
    version="1.0.0"
)

app.include_router(api_router)
