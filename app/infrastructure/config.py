import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL") or "sqlite:///./sql_app.db"
    DATABASE_TEST: bool = (os.getenv("DATABASE_TEST")
                           or "False").lower() == "true"
    DATABASE_TEST_URL = "sqlite:///./test.db"
    ORIGINS: str = os.getenv(
        "APP_CONFIG_ORIGINS") or '["http://localhost:3000"]'
    METHODS: str = os.getenv("APP_CONFIG_METHODS") or '["*"]'
    HEADERS: str = os.getenv("APP_CONFIG_HEADERS") or '["*"]'
    CREDENTIALS: bool = (os.getenv("APP_CONFIG_CREDENTIALS")
                         or "True").lower() == "true"
    SECRET_KEY = os.getenv(
        "SECRET_KEY") or "52596af96fd3b11c4bcb0181e8050607131dfb9f01ef52309603c65e0103e141"
    ALGORITHM = os.getenv("ALGORITHM") or "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES") or 30)
    SERVER_HOST = os.getenv("SERVER_HOST") or "example.com"


settings = Settings()
