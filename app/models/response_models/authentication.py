from pydantic import BaseModel

class AuthenticationResponse(BaseModel):
    access_token: str
    token_type: str = "Bearer"