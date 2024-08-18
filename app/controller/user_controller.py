from app.dependencies.user_dependency import get_user_register_uc
from app.mapper.user_mapper import UserMapper
from app.repository.implementation.user_repository import UserRepository
from app.service.user_service import UserService
from app.tags import USER_TAG
from fastapi import APIRouter, Body, Depends, status
from sqlalchemy.orm import Session

from app.application.user_register_uc import UserRegisterUseCase
from app.dependencies.database_dependency import get_db
from app.models.request_models.register_user import RegisterUserRequest
from app.models.response_models.register_user import RegisterUserResponse
from app.utils.security import HashValidator

router = APIRouter()


@router.post("/register", tags=[USER_TAG], status_code=status.HTTP_201_CREATED)
async def read_users(
    request: RegisterUserRequest = Body(...), 
    user_uc: UserRegisterUseCase = Depends(get_user_register_uc)
    ) -> RegisterUserResponse:
    user_dto = UserMapper().request_to_dto(request=request)
    return user_uc.execute(user=user_dto)