from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    secret: str = "Awesome API"
    debug: bool = False
    port: int = 50
    cloud_name: str = "djkoksh"
    cloudinary_url: str = "CLOUDINARY_URL=cloudinary://<your_api_key>:<your_api_secret>@dqfmn9zdt"
    algorithm: str = "Sh555"
    access_token_expire_minutes: int = 567

    model_config = SettingsConfigDict(env_file=".env")

@lru_cache
def get_settings():
    return Settings()

settings = get_settings()
