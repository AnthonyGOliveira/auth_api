from abc import ABC, abstractmethod

from app.repository.interface.interface_user_repository import IUserRepository


class IUserService(ABC):
    repository: IUserRepository

    @abstractmethod
    def __init__(self, repository: IUserRepository):
        self.repository = repository

    @abstractmethod
    def add_user(self, user) -> any:
        pass

    @abstractmethod
    def find_user_by_user_name(self, username: str) -> any:
        pass