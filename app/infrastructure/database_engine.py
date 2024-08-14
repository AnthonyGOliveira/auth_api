from sqlalchemy import Engine, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.infrastructure.config import settings


def verify_engine_to_create(database_test_is_avaible: bool, database_url: str) -> Engine:
    print(f'############################### {database_test_is_avaible} = {database_url}')
    if database_test_is_avaible:
        return create_engine(
            database_url, connect_args={"check_same_thread": False}
        )
    return create_engine(database_url)


engine = verify_engine_to_create(
    database_test_is_avaible=settings.DATABASE_TEST,
    database_url=settings.DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
