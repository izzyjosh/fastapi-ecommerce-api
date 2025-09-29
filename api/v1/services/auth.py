from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi import status
from sqlalchemy import Select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from pwdlib import PasswordHash
from api.v1.schemas.user import UserCreateSchema, UserResponseModel
from api.v1.models.user import User


class AuthService:

    password_hash = PasswordHash.recommended()

    def verify_password(self, plain_password, hashed_password):
        return self.password_hash.verify(plain_password, hashed_password)


    def get_password_hash(self, password):
        return self.password_hash.hash(password)


    def register(self, db: Session, user: UserCreateSchema):
        stmt = Select(User).where((User.email == user.email) | (User.username == user.username))
        existing_user = db.scalars(stmt).first()

        if existing_user:
            if existing_user.email == user.email:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this email already exist")
            if existing_user.username == user.username:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user with this username already exists")

        # Get hased password
        hashed_password = self.get_password_hash(user.password)

        new_user = User(username=user.username, email=user.email, password=hashed_password)
        db.add(new_user)

        # Use the try to handle integrity error from db
        try:
            db.commit()
            db.refresh(new_user)

        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="username or email already exist")

        return UserResponseModel.model_validate(new_user, from_attributes=True)

