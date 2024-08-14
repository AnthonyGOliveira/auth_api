from fastapi import APIRouter, Body, Depends, status
from sqlalchemy.orm import Session

from app.application.user_register_uc import UserRegisterUseCase
from app.dependencies.database_dependency import get_db
from app.models.database_models.user import User
from app.models.request_models.register_user import RegisterUserRequest
from app.models.response_models.register_user import RegisterUserResponse
from app.utils.security import HashValidator

router = APIRouter()


@router.post("/register", tags=["USER_TAG"], status_code=status.HTTP_201_CREATED)
async def read_users(request: RegisterUserRequest = Body(...), db: Session = Depends(get_db)) -> RegisterUserResponse:
    db_user = User(
        username=request.username,
        email=request.email,
        password=request.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    # validator = HashValidator()
    # use_case = UserRegisterUseCase(validator=validator)
    # return use_case.execute(request=request)
