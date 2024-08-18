from app.dto.dto_interface import IDto


class UserDto(IDto):
    username: str
    email: str
    password: str
    
    def __init__(self, **kwargs) -> None:
        self.username = kwargs.get('username')
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')