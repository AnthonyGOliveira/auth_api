from fastapi import HTTPException, status


class UserAlreadyExistsException(HTTPException):
    def __init__(self, detail: str = "Username or email already exists"):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=detail)


class UserPasswordException(HTTPException):
    def __init__(self, detail: str = "Password exception"):
        super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=detail)
        
        
class UserEmailException(HTTPException):
    def __init__(self, detail: str = "Email exception"):
        super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=detail)
        
class UsernameOrPasswordIncorrectException(HTTPException):
    def __init__(self, detail: str = "Username or password is incorrect"):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)