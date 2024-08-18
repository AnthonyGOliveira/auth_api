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


settings = Settings()
