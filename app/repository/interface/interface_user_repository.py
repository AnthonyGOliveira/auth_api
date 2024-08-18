from abc import ABC, abstractmethod

from app.dto.dto_interface import IDto


class IUserRepository(ABC):

    @abstractmethod
    def __init__(self, db) -> None:
        self.db = db

    @abstractmethod
    def add_user(self, user: IDto) -> any:
        pass
