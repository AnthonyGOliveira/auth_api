import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL") or "sqlite:///./sql_app.db"
    DATABASE_TEST: bool = (os.getenv("DATABASE_TEST")
                           or "False").lower() == "true"


settings = Settings()
