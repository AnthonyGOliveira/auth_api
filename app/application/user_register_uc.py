from app.dto.dto_interface import IDto
from app.dto.user_dto import UserDto
from app.service.interface.interface_user_service import IUserService
from app.utils.interface_security import IHashValidator


class UserRegisterUseCase:
    validator: IHashValidator
    service: IUserService

    def __init__(self, validator: IHashValidator, service: IUserService):
        self.validator = validator
        self.service = service

    def execute(self, user: IDto):

        hash_password = self.validator.hash_password(password=user.password)
        user.password = hash_password
        return self.service.add_user(user=user)
