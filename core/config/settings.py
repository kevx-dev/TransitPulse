from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    latitude: float
    longitude: float
    telegram_api_key: str
    telegram_chat_id: str

    class Config:
        env_file = ".env"