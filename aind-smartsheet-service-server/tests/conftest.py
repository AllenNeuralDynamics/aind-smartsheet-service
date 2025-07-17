"""Set up fixtures to be used across all test modules."""

import json
import os
from pathlib import Path
from typing import Any, Generator
from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient
from pydantic import RedisDsn

from aind_smartsheet_service_server.configs import get_settings

RESOURCES_DIR = Path(os.path.dirname(os.path.realpath(__file__))) / "resources"

patch(
    "fastapi_cache.decorator.cache", lambda *args, **kwargs: lambda f: f
).start()


@pytest.fixture()
def mock_raw_funding_sheet() -> str:
    """Raw funding sheet."""
    with open(RESOURCES_DIR / "funding.json") as f:
        contents = json.load(f)
    return json.dumps(contents)


@pytest.fixture()
def mock_raw_protocols_sheet() -> str:
    """Expected raw protocols sheet."""
    with open(RESOURCES_DIR / "protocols.json") as f:
        contents = json.load(f)
    return json.dumps(contents)


@pytest.fixture()
def mock_raw_perfusions_sheet() -> str:
    """Expected raw protocols sheet."""
    with open(RESOURCES_DIR / "perfusions.json") as f:
        contents = json.load(f)
    return json.dumps(contents)


@pytest.fixture(scope="session")
def client() -> Generator[TestClient, Any, None]:
    """Creating a client for testing purposes."""

    # Import moved to be able to mock cache
    from aind_smartsheet_service_server.main import app

    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="function")
def client_with_redis() -> Generator[TestClient, Any, None]:
    """Creating a client when settings have a redis_url. Only used in one test
    to verify the lifespan method in main is called correctly."""

    # Import moved to be able to mock cache
    from aind_smartsheet_service_server.main import app

    settings = get_settings()
    settings_with_redis = settings.model_copy(
        update={"redis_url": RedisDsn("redis://example.com:1234")}, deep=True
    )
    with (
        patch(
            "aind_smartsheet_service_server.main.get_settings",
            return_value=settings_with_redis,
        ),
        patch(
            "aind_smartsheet_service_server.main.from_url", return_value=None
        ),
        patch(
            "aind_smartsheet_service_server.main.RedisBackend",
            return_value=None,
        ),
    ):
        with TestClient(app) as c:
            yield c
