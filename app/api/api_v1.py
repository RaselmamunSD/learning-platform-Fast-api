from fastapi import APIRouter
from app.modules.user import routes as user_routes
from app.modules.auth import routes as auth_routes

api_router = APIRouter()

api_router.include_router(user_routes.router, prefix="/users", tags=["users"])
api_router.include_router(auth_routes.router, prefix="/auth", tags=["auth"])
