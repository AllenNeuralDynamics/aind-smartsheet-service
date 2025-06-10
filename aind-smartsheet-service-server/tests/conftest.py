"""Set up fixtures to be used across all test modules."""

import json
import os
from pathlib import Path
from typing import Any, Generator
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient
from pytest_mock import MockFixture

from aind_smartsheet_service_server.main import app

RESOURCES_DIR = Path(os.path.dirname(os.path.realpath(__file__))) / "resources"


def mock_raw_sheet(mocker: MockFixture, path: Path) -> MagicMock:
    """Mocks a get raw sheet call."""
    with open(path) as f:
        contents = json.load(f)
    mock_get = mocker.patch(
        "aind_smartsheet_api.client.SmartsheetClient.get_raw_sheet"
    )
    mock_get.return_value = json.dumps(contents)
    return mock_get


@pytest.fixture()
def mock_get_raw_funding_sheet(mocker: MockFixture) -> MagicMock:
    """Expected raw funding sheet."""
    return mock_raw_sheet(mocker, RESOURCES_DIR / "funding.json")


@pytest.fixture()
def mock_get_raw_protocols_sheet(mocker: MockFixture) -> MagicMock:
    """Expected raw protocols sheet."""
    return mock_raw_sheet(mocker, RESOURCES_DIR / "protocols.json")


@pytest.fixture()
def mock_get_raw_perfusions_sheet(mocker: MockFixture) -> MagicMock:
    """Expected raw protocols sheet."""
    return mock_raw_sheet(mocker, RESOURCES_DIR / "perfusions.json")


@pytest.fixture(scope="session")
def client() -> Generator[TestClient, Any, None]:
    """Creating a client for testing purposes."""

    with TestClient(app) as c:
        yield c
