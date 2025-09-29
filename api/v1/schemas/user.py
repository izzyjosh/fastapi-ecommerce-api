from datetime import datetime
from typing import Literal
from uuid import UUID
from pydantic import BaseModel, ConfigDict, EmailStr, Field

class UserCreateSchema(BaseModel):
    username: str = Field(max_length=50)
    email: EmailStr
    password: str


class UserResponseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    username: str
    email: str
    profile_pic: str
    verified: bool
    is_active: bool
    role: Literal["customer", "admin", "seller"]
    last_login: datetime
