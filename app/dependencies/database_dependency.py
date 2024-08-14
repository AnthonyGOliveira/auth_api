from app.infrastructure.database_engine import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()