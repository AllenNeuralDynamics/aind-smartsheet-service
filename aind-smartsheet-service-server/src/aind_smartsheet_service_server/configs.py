"""Module for settings to connect to backend"""

from typing import Optional

from aind_settings_utils.aws import (
    ParameterStoreAppBaseSettings,
)
from pydantic import Field, SecretStr
from pydantic_settings import SettingsConfigDict


class Settings(ParameterStoreAppBaseSettings):
    """Smartsheet configs with client settings and sheet IDs"""

    access_token: SecretStr = Field(
        ..., description="API token. Can be created in Smartsheet UI."
    )
    user_agent: Optional[str] = Field(
        default="aind-smartsheet-service-server",
        description=(
            "The user agent to use when making requests. "
            "Helps identify requests."
        ),
    )
    max_connections: int = Field(
        default=8, description="Maximum connection pool size."
    )
    funding_id: int = Field(..., description="SmartSheet ID of funding info")
    perfusions_id: int = Field(
        ..., description="SmartSheet ID of perfusions info"
    )
    protocols_id: int = Field(
        ..., description="SmartSheet ID of protocols info"
    )
    redis_url: Optional[str] = Field(default=None)
    model_config = SettingsConfigDict(
        env_prefix="SMARTSHEET_", case_sensitive=False
    )


def get_settings() -> Settings:
    """Return a settings object"""
    return Settings()
