from api.v1.utils.storage import SessionLocal

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
