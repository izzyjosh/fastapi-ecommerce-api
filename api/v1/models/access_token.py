from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, foreign, mapped_column, relationship
from api.v1.models.abstract_base import AbstractBase
from datetime import datetime
from uuid import UUID

class AccessToken(AbstractBase):
    __tablename__ = "access_token"

    token: Mapped[str]
    blacklisted: Mapped[bool] = mapped_column(default=False)
    expiry_time: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    user = relationship("User", back_populates="access_tokens")

    def __repr__(self) -> str:
        return self.token
