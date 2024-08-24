from fastapi import APIRouter, Body, Depends, status

from app.application.authentication_uc import AuthenticationUseCase
from app.dependencies.authentication_dependency import get_authentication_uc
from app.mapper.authentication_mapper import AuthenticationMapper
from app.models.request_models.authentication import AuthenticationRequest
from app.models.response_models.register_user import RegisterUserResponse
from app.tags import AUTHETICATION_TAG

router = APIRouter()


@router.post("/login", tags=[AUTHETICATION_TAG], status_code=status.HTTP_200_OK)
async def login(
    request: AuthenticationRequest = Body(...),
    authentication_uc: AuthenticationUseCase = Depends(get_authentication_uc)
) -> RegisterUserResponse:

    authentication_dto = AuthenticationMapper().request_to_dto(request=request)
    return authentication_uc.execute(authentication_request=authentication_dto)
