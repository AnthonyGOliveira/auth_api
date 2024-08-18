from app.application.user_register_uc import UserRegisterUseCase
from app.repository.implementation.user_repository import UserRepository
from app.service.user_service import UserService
from app.utils.security import HashValidator
from sqlalchemy.orm import Session
from fastapi import Depends
from app.dependencies.database_dependency import get_db

def get_user_register_uc(db: Session = Depends(get_db)) -> UserRegisterUseCase:
    validator = HashValidator()
    user_repository = UserRepository(db=db)
    user_service = UserService(repository=user_repository)
    return UserRegisterUseCase(validator=validator, service=user_service)
