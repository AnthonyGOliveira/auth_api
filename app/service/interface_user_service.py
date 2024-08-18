from abc import ABC, abstractmethod

from app.repository.interface.interface_user_repository import IUserRepository


class IUserService(ABC):
    repository: IUserRepository

    @abstractmethod
    def __init__(self, repository: IUserRepository):
        self.repository = repository

    @abstractmethod
    def execute(self, user) -> any:
        pass
