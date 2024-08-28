from fastapi import Depends
from sqlalchemy.orm import Session

from app.application.authentication_uc import AuthenticationUseCase
from app.dependencies.database_dependency import get_db
from app.repository.implementation.user_repository import UserRepository
from app.service.implementation.secret_service import SecretService
from app.service.implementation.user_service import UserService
from app.utils.security import HashValidator


def get_authentication_uc(db: Session = Depends(get_db)) -> AuthenticationUseCase:
    validator = HashValidator()
    user_repository = UserRepository(db=db)
    user_service = UserService(repository=user_repository)
    secret_service = SecretService()
    return AuthenticationUseCase(validator=validator, service=user_service, secret_service=secret_service)
