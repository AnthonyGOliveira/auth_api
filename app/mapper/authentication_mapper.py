from app.dto.authentication_dto import AuthenticationDto
from app.mapper.mapper_interface import IMapper
from app.models.request_models.authentication import AuthenticationRequest


class AuthenticationMapper(IMapper):
    def request_to_dto(self, request: AuthenticationRequest) -> AuthenticationDto:
        return AuthenticationDto(**dict(request))