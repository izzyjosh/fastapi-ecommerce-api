# Python
from datetime import datetime, timedelta, timezone
from os import access

# External
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from pwdlib import PasswordHash
from sqlalchemy.exc import IntegrityError
from uuid import UUID
import jwt
# Internal
from api.v1.schemas.user import UserCreateSchema
from api.v1.models.user import User
from api.v1.models.access_token import AccessToken
from utils.config import settings


class UserService:

    password_hasher = PasswordHash.recommended()
    
    def create(self, db: Session, user: UserCreateSchema):
        # Ch3ck if user already exist

        existing_user = db.scalars(select(User).where((User.email == user.email) | (User.username == user.username))).first()

        if existing_user:
            if existing_user.email == user.email:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this email already exists")
            if existing_user.username == user.username:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this username already exists")

        hashed_password = self.hash_password(user.password)
        user.password = hashed_password

        new_user = User(**user.model_dump())

        db.add(new_user)

        try:
            db.commit()
            db.refresh(new_user)
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="email or usernme already exists")

        token, expiry = self.generate_access_token(db, new_user).values()

        user = jsonable_encoder(self.get_user_details(db=db, user_id=new_user.id), exclude={"password"})
        response = {
                "access_token": token,
                "expiry_time": expiry,
                "user": user
                }
        return response


    def handle_login(self, db: Session, email: str, password: str):
        user = self.get_user_by_email(db=db, email=email)

        if not user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User does not exists")

        if not self.verify_password(password, user.password):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="ivalid password")

        access_token, expiry = self.generate_access_token(db=db, user=user).values()

        user.last_login = datetime.now(timezone.utc)

        db.commit()
        db.refresh(user)

        user = jsonable_encoder(self.get_user_details(db, user.id), exclude={"password"})

        response = {
                "access_token": access_token,
                "expiry": expiry,
                "user": user
                }

        return response


    def get_user_by_email(self, db: Session, email: str):
        stmt = select(User).where(User.email == email)
        result = db.scalars(stmt).first()
        return result



    def get_user_details(self, db: Session, user_id: UUID):
        stmt = select(User).where(User.id == user_id)
        result = db.scalars(stmt).first()
        return result


    def generate_access_token(self, db: Session, user: User):
        payload = {
                "email": user.email,
                "role": user.role.value,
                "username": user.username
                }
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)

        payload.update({"exp": expire})
        token = jwt.encode(payload, settings.secret, algorithm=settings.algorithm)

        access_token = AccessToken(user_id=user.id, token=token, expiry_time=expire)
        db.add(access_token)
        db.commit()
        db.refresh(access_token)

        return {"access_token": token, "expiry_time": expire}


    def verify_password(self, password, hashed_password):
        return self.password_hasher.verify(password, hashed_password)


    def hash_password(self, password: str) -> str:
        return self.password_hasher.hash(password)


user_service = UserService()
