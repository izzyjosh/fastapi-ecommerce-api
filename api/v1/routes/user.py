from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from api.v1.schemas.user import UpdateRole
from api.v1.services.user import user_service
from api.v1.services.user import admin_required
from api.v1.responses.success_response import success_response
from api.v1.utils.dependencies import get_db

user = APIRouter(prefix="/users", tags=["user"])


@user.patch("/{user_id}/role", dependencies=[Depends(admin_required)])
async def update_user_role(user_id: UUID, role: UpdateRole, db: Annotated[Session, Depends(get_db)]):
    user = user_service.update_role(user_id=user_id, role=role, db=db)
    response = jsonable_encoder(user)

    return success_response(message="User role updated successfully", data=response)

