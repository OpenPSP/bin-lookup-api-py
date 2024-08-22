from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class ProjectSettings(BaseSettings):
    name: str = Field(default="BIN Lookup API", alias="PROJECT_NAME")
    description: str = Field(default="API for looking up BIN information", alias="PROJECT_DESCRIPTION")
    version: str = Field(default="0.1.0", alias="PROJECT_VERSION")

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

class RedisSettings(BaseSettings):
    host: str = Field(default="localhost", alias="REDIS_HOST")
    port: int = Field(default=6379, alias="REDIS_PORT")
    db: int = Field(default=0, alias="REDIS_DB")
    password: Optional[str] = Field(default=None, alias="REDIS_PASSWORD")

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

class LogSettings(BaseSettings):
    level: str = Field(default="INFO", alias="LOG_LEVEL")
    format: str = Field(default=(
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
    ), alias="LOG_FORMAT")
    logger_name: str = Field(default="", alias="LOGGER_NAME")

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


class IndexSettings(BaseSettings):
    file_path: str = Field(default="", alias="INDEX_FILE_PATH")

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


class AppSettings(BaseSettings):
    project: ProjectSettings = ProjectSettings()
    redis: RedisSettings = RedisSettings()
    log: LogSettings = LogSettings()
    index: IndexSettings = IndexSettings()

# Instantiate the settings
settings = AppSettings()
