from pydantic import BaseModel
from datetime import datetime


class RegisterUserResponse(BaseModel):
    id: str
    username: str
    email: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True
