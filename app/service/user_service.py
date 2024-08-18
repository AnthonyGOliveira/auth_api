from app.dto.user_dto import UserDto
from app.mapper.user_mapper import UserMapper
from app.repository.interface.interface_user_repository import IUserRepository
from app.service.interface_user_service import IUserService


class UserService(IUserService):

    def __init__(self, repository: IUserRepository):
        super().__init__(repository)

    def execute(self, user: UserDto) -> any:
        return self.repository.add_user(user=user)
