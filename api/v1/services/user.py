
from sqlalchemy.orm import Session

class UserService:
    async def create(self, db: Session, body: dict):



user_service = UserService()
