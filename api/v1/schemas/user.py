from datetime import datetime
import enum
from typing import Literal
from uuid import UUID
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from pydantic_core.core_schema import SerializerFunctionWrapHandler

class UserCreateSchema(BaseModel):
    username: str = Field(max_length=50)
    email: EmailStr
    password: str


class RoleEnum(str, enum.Enum):
    customer = "customer"
    admin = "admin"
    seller = "seller"


class UserResponseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    username: str
    email: str
    profile_pic: str | None
    verified: bool
    is_active: bool
    role: RoleEnum
    last_login: datetime | None

class LoginSchema(BaseModel):
    email: str
    password: str

class UpdateRole(BaseModel):
    role: Literal["customer", "admin", "seller"]
