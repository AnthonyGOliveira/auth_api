from app.dto.dto_interface import IDto
from app.exceptions.user_exceptions import UsernameOrPasswordIncorrectException
from app.service.interface_user_service import IUserService
from app.utils.interface_security import IHashValidator


class AuthenticationUseCase:
    validator: IHashValidator
    service: IUserService

    def __init__(self, validator: IHashValidator, service: IUserService):
        self.validator = validator
        self.service = service

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

        return user
