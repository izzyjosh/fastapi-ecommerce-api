from typing import Annotated
from fastapi.exceptions import HTTPException
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from api.v1.schemas.user import LoginSchema, UserCreateSchema
from api.v1.schemas.auth import Token
from api.v1.utils.dependencies import get_db
from api.v1.services.auth import auth_service
from api.v1.responses.success_response import success_response
from api.v1.services.user import user_service
from datetime import timedelta
from utils.config import settings

auth = APIRouter(prefix="/auth", tags=["auth"])

@auth.post("/register", status_code=status.HTTP_201_CREATED)
async def create_user(db: Annotated[Session, Depends(get_db)], user: UserCreateSchema):

    response = user_service.create(db=db, user=user)

    return success_response(status_code=status.HTTP_201_CREATED, message="user created successfully", data=response)


@auth.post("/login")
async def login_for_access_token(auth_data: LoginSchema, db: Annotated[Session, Depends(get_db)]):

    response = user_service.handle_login(db=db, email=auth_data.email, password=auth_data.password)

    return success_response(status_code=status.HTTP_200_OK, message="Logged In successfully", data=response)
