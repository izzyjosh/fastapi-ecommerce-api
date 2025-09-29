from fastapi import APIRouter
from api.v1.routes.user import user
from api.v1.routes.auth import auth

version_one = APIRouter(prefix="/api/v1")

version_one.include_router(user)
version_one.include_router(auth)
