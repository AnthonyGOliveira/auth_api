from fastapi import APIRouter, Body, status

from app.models.request_models.register_user import RegisterUserRequest

router = APIRouter()


@router.post("/register", tags=["USER_TAG"], status_code=status.HTTP_201_CREATED)
async def read_users(request: RegisterUserRequest = Body(...)):
    return request
