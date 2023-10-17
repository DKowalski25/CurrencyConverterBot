from pydantic_settings import BaseSettings
from config import HOST, PORT, POSTGRES_URL


class Settings(BaseSettings):
    server_host: str = HOST
    server_port: int = PORT
    database_url: str = POSTGRES_URL


settings = Settings()
