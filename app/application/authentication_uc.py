from app.dto.dto_interface import IDto
from app.exceptions.user_exceptions import UsernameOrPasswordIncorrectException
from app.service.interface.interface_secret_service import ISecretService
from app.service.interface.interface_user_service import IUserService
from app.utils.interface_security import IHashValidator


class AuthenticationUseCase:
    validator: IHashValidator
    service: IUserService
    secret_service: ISecretService

    def __init__(self, validator: IHashValidator, service: IUserService, secret_service: ISecretService):
        self.validator = validator
        self.service = service
        self.secret_service = secret_service

    def execute(self, authentication_request: IDto):
        user = self.service.find_user_by_user_name(
            username=authentication_request.username
        )
        if user is None:
            raise UsernameOrPasswordIncorrectException()

        password_is_valid = self.validator.verify_password(
            plain_password=authentication_request.password,
            hashed_password=user.password
        )
        if password_is_valid is False:
            raise UsernameOrPasswordIncorrectException()
        user_dict = {
            "sub": user.username,
            "email": user.email
        }
        return {
            "access_token": self.secret_service.create_access_token(data=user_dict),
        }
