from app.models.request_models.register_user import RegisterUserRequest
from app.models.response_models.register_user import RegisterUserResponse
from app.utils.interface_security import IHashValidator


class UserRegisterUseCase:
    validator: IHashValidator

    def __init__(self, validator: IHashValidator):
        self.validator = validator

    def execute(self, request: RegisterUserRequest):

        hash_password = self.validator.hash_password(password=request.password)
        password_is_valid = self.validator.verify_password(
            plain_password=request.password, hashed_password=hash_password)

        return RegisterUserResponse(
            username=request.username,
            email=request.email,
            password=request.password,
            password_is_valid=password_is_valid,
            hash_password=hash_password
        )
