from typing import Annotated
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from api.v1.schemas.user import UserCreateSchema
from api.v1.utils.dependencies import get_db
from 

auth = APIRouter(prefix="/auth", tags=["auth"])

@auth.post("/register", status_code=status.HTTP_201_CREATED)
async def create_user(db: Annotated[Session, Depends(get_db)], user: UserCreateSchema):



