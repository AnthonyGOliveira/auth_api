from app.dto.dto_interface import IDto


class AuthenticationDto(IDto):
    username: str
    password: str

    def __init__(self, **kwargs) -> None:
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
