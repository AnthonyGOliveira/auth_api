from app.utils.interface_security import IHashValidator
import bcrypt


class HashValidator(IHashValidator):
    salt: bytes

    def __init__(self):
        self.salt = bcrypt.gensalt()

    def hash_password(self, password: str) -> str:
        password_bytes = self._format_str_to_bytes(data=password)
        hash_password = bcrypt.hashpw(
            password=password_bytes,
            salt=self.salt
        )
        return self._format_bytes_to_str(data=hash_password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        password_bytes = self._format_str_to_bytes(data=plain_password)
        hashed_password_bytes = self._format_str_to_bytes(
            data=hashed_password)
        check = bcrypt.checkpw(
            password=password_bytes,
            hashed_password=hashed_password_bytes
        )
        return check

    def _format_str_to_bytes(self, data: str) -> bytes:
        return data.encode('utf-8')

    def _format_bytes_to_str(self, data: bytes) -> str:
        return data.decode('utf-8')
