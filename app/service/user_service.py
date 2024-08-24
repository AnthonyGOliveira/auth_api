from fastapi import HTTPException, status
from app.dto.user_dto import UserDto
from app.exceptions.user_exceptions import UserAlreadyExistsException
from app.mapper.user_mapper import UserMapper
from app.models.database_models.user import User
from app.repository.interface.interface_user_repository import IUserRepository
from app.service.interface_user_service import IUserService
from sqlalchemy.exc import IntegrityError


class UserService(IUserService):

    def __init__(self, repository: IUserRepository):
        super().__init__(repository)

    def add_user(self, user: UserDto) -> any:
        try:
            return self.repository.add_user(user=user)
        except IntegrityError as error:
            if "UNIQUE constraint failed:" in str(error.orig):
                raise UserAlreadyExistsException()
            else:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Internal Server Error"
                )

    def find_user_by_user_name(self, username: str) -> any:
        return self.repository.find_user_by_user_name(username=username)
