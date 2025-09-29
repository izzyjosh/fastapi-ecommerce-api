from pydantic import BaseModel, EmailStr


class AuthBase(BaseModel):
    username: str
    email: EmailStr
    password: str

