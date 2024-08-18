from abc import ABC, abstractmethod
from app.dto.dto_interface import IDto
from app.models.database_models.interface_database_model import IDatabaseModel
from pydantic import BaseModel

class IMapper(ABC):
    
    @abstractmethod
    def request_to_dto(self, request: BaseModel) -> IDto:
        pass