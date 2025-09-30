from datetime import datetime
from typing import Optional
import enum
from sqlalchemy import Boolean, DateTime, Enum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from api.v1.models.abstract_base import AbstractBase

class RoleEnum(enum.Enum):
    customer = "customer"
    admin = "admin"
    seller = "seller" 


class User(AbstractBase):

    __tablename__: str = "users"

    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(225), unique=True, index=True)
    profile_pic: Mapped[Optional[str]] = mapped_column(String(225))
    verified: Mapped[bool] = mapped_column(Boolean, default=False, server_default="false")
    is_active: Mapped[bool] = mapped_column(Boolean, default=False, server_default="false")
    role: Mapped[RoleEnum] = mapped_column(Enum(RoleEnum), name="role_enum", default=RoleEnum.customer)
    password: Mapped[str] = mapped_column(String(225))
    last_login: Mapped[Optional[datetime]] = mapped_column(DateTime)

    access_tokens: Mapped[list] = relationship("AccessToken", back_populates="user")


    def __repr__(self) -> str:
        return f"{self.role}: {self.username} -> {self.email}"
