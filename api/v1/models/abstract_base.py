from datetime import datetime
import uuid
from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from api.v1.utils.storage import Base

class AbstractBase(Base):
    __abstract__: bool= True

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4())
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())
