from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from app.infrastructure.config import settings

engine = create_engine(settings.DATABASE_URL, echo=True, connect_args={
    "check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
