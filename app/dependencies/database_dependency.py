from app.infrastructure.database_engine import Base, SessionLocal, engine


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_test_db():
    Base.metadata.create_all(bind=engine)
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)
