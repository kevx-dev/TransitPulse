from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    latitude: float
    longitude: float

    class Config:
        env_file = ".env"