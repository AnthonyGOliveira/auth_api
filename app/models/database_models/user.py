from datetime import datetime, timezone
from app.models.database_models.interface_database_model import IDatabaseModel
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from app.infrastructure.database_engine import Base
import uuid


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True,
                default=lambda: str(uuid.uuid4()))
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
