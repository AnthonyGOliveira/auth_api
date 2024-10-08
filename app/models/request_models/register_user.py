import re
from app.exceptions.user_exceptions import UserEmailException, UserPasswordException
from pydantic import BaseModel, field_validator, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str

    @field_validator("password")
    def validate_password(cls, password):
        # Common passwords
        common_passwords = ["password", "123456",
                            "123456789", "qwerty", "abc123"]
        if password in common_passwords:
            raise UserPasswordException("Password is too common.")
        
        # Sequences
        if re.search(r"(0123456789|abcdefghijklmnopqrstuvwxyz|ABCDEFGHIJKLMNOPQRSTUVWXYZ)", password):
            raise UserPasswordException("Password cannot contain simple sequences.")
        
        if len(password) < 8:
            raise UserPasswordException("Password must be at least 8 characters long.")

        # Uppercase and lowercase letters
        if not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password):
            raise UserPasswordException(
                "Password must contain at least one uppercase and one lowercase letter.")

        # Numbers
        if not re.search(r"\d", password):
            raise UserPasswordException("Password must contain at least one number.")

        # Special characters
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise UserPasswordException(
                "Password must contain at least one special character.")

        return password

    @field_validator("email")
    def validate_email(cls, email):
        # Prohibited domains
        forbidden_domains = ["example.com", "test.com"]
        domain = email.split('@')[1]
        if domain in forbidden_domains:
            raise UserEmailException("Email domain is not allowed.")

        # Maximum length
        if len(email) > 256:
            raise UserEmailException("Email must be at most 256 characters long.")

        return email


class RegisterUserRequest(UserCreate):
    username: str
