from app.dto.dto_interface import IDto
from app.models.database_models.user import User
from app.repository.interface.interface_user_repository import IUserRepository


class UserRepository(IUserRepository):

    def __init__(self, db) -> None:
        super().__init__(db)

    def add_user(self, user: IDto) -> any:
        user_model = User(
            username=user.username,
            email=user.email,
            password=user.password,
        )
        self.db.add(user_model)
        self.db.commit()
        self.db.refresh(user_model)
        return user_model
