from fastapi import APIRouter, Body, status

from app.application.user_register_uc import UserRegisterUseCase
from app.models.request_models.register_user import RegisterUserRequest
from app.models.response_models.register_user import RegisterUserResponse
from app.utils.security import HashValidator

router = APIRouter()


@router.post("/register", tags=["USER_TAG"], status_code=status.HTTP_201_CREATED)
async def read_users(request: RegisterUserRequest = Body(...)) -> RegisterUserResponse:
    validator = HashValidator()
    use_case = UserRegisterUseCase(validator=validator)
    return use_case.execute(request=request)
