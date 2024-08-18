from app.dto.user_dto import UserDto
from app.mapper.mapper_interface import IMapper
from app.models.database_models.user import User
from app.models.request_models.register_user import RegisterUserRequest


class UserMapper(IMapper):

    def request_to_dto(self, request: RegisterUserRequest) -> UserDto:
        return UserDto(**dict(request))

    def dto_to_model(self, user_dto: UserDto) -> User:
        return User(
            username=user_dto.username,
            email=user_dto.email,
            password=user_dto.password,
        )
