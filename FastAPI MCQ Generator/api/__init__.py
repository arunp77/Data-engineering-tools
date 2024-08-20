# api/__init__.py

# Import modules to make them available when the package is imported
from api.endpoints import router as api_router
from api.auth import authenticate
from api.models import Question