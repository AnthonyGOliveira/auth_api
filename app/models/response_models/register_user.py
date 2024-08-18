from pydantic import BaseModel, ConfigDict
from datetime import datetime


class RegisterUserResponse(BaseModel):
    id: str
    username: str
    email: str
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )
