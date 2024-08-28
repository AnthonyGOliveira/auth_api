from datetime import datetime, timedelta, timezone
from app.service.interface.interface_secret_service import ISecretService
from app.infrastructure.config import settings
import jwt
import socket


class SecretService(ISecretService):

    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(
                timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({
            "exp": expire,
            "iss": self.get_iss()
        })
        encoded_jwt = jwt.encode(
            to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt

    def get_iss(self):
        hostname = socket.gethostname()  # Obtém o hostname do servidor
        # Exemplo de domínio ou URL base
        domain = settings.SERVER_HOST
        return f"https://{hostname}.{domain}"