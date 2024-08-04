from pydantic import BaseModel


class RegisterUserResponse(BaseModel):
    username: str
    email: str
    password: str
    password_is_valid: bool
    hash_password: bytes
