"""Module to test main app"""

from unittest.mock import MagicMock

import pytest
from starlette.testclient import TestClient


class TestMain:
    """Tests app endpoints"""

    def test_get_healthcheck(self, client: TestClient):
        """Tests healthcheck"""
        response = client.get("/healthcheck")
        assert 200 == response.status_code

    def test_get_funding(
        self, client: TestClient, mock_get_raw_funding_sheet: MagicMock
    ):
        """Tests funding"""
        response = client.get("/funding")
        assert 200 == response.status_code

    def test_get_project_names(
        self, client: TestClient, mock_get_raw_funding_sheet: MagicMock
    ):
        """Tests project_names"""
        response = client.get("/project_names")
        assert 200 == response.status_code

    def test_get_protocols(
        self, client: TestClient, mock_get_raw_protocols_sheet: MagicMock
    ):
        """Tests protocols"""
        response = client.get("/protocols")
        assert 200 == response.status_code

    def test_get_perfusions(
        self, client: TestClient, mock_get_raw_perfusions_sheet: MagicMock
    ):
        """Tests perfusions"""
        response = client.get("/perfusions")
        assert 200 == response.status_code


if __name__ == "__main__":
    pytest.main([__file__])
