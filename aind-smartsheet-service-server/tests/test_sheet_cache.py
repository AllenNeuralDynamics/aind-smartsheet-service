"""Tests sheet_cache module"""

from unittest.mock import AsyncMock, patch

import httpx
import pytest
from fastapi import HTTPException

from aind_smartsheet_service_server.sheet_cache import fetch_sheet
from tests.conftest import RESOURCES_DIR


@pytest.fixture()
def funding_json() -> bytes:
    """Raw funding sheet bytes as returned by the Smartsheet REST API."""
    return (RESOURCES_DIR / "funding.json").read_bytes()


class TestFetchSheet:
    """Tests fetch_sheet"""

    @patch("httpx.AsyncClient.get")
    async def test_fetch_sheet(self, mock_get: AsyncMock, funding_json):
        """Tests a successful download sends auth headers and parses JSON"""
        mock_get.return_value = httpx.Response(200, content=funding_json)
        sheet = await fetch_sheet(
            sheet_id=100, user_agent="agent", access_token="token"
        )
        assert sheet.rows
        url = mock_get.call_args.args[0]
        headers = mock_get.call_args.kwargs["headers"]
        assert url.endswith("/sheets/100")
        assert headers == {
            "Authorization": "Bearer token",
            "User-Agent": "agent",
        }

    @patch("httpx.AsyncClient.get")
    async def test_fetch_sheet_no_user_agent(
        self, mock_get: AsyncMock, funding_json
    ):
        """Tests no User-Agent header is set when user_agent is empty"""
        mock_get.return_value = httpx.Response(200, content=funding_json)
        await fetch_sheet(sheet_id=100, user_agent=None, access_token="token")
        headers = mock_get.call_args.kwargs["headers"]
        assert headers == {"Authorization": "Bearer token"}

    @patch("aind_smartsheet_service_server.sheet_cache.sleep")
    @patch("httpx.AsyncClient.get")
    async def test_fetch_sheet_retries(
        self, mock_get: AsyncMock, mock_sleep: AsyncMock, funding_json
    ):
        """Tests rate limit and server errors are retried"""
        mock_get.side_effect = [
            httpx.Response(429),
            httpx.Response(503),
            httpx.Response(200, content=funding_json),
        ]
        sheet = await fetch_sheet(
            sheet_id=100, user_agent="agent", access_token="token"
        )
        assert sheet.rows
        assert mock_get.await_count == 3
        assert [c.args[0] for c in mock_sleep.await_args_list] == [1, 2]

    @patch("aind_smartsheet_service_server.sheet_cache.sleep")
    @patch("httpx.AsyncClient.get")
    async def test_fetch_sheet_retries_exhausted(
        self, mock_get: AsyncMock, mock_sleep: AsyncMock
    ):
        """Tests the last error is raised once retries are used up"""
        mock_get.return_value = httpx.Response(
            503, json={"message": "Service unavailable"}
        )
        with pytest.raises(HTTPException) as e:
            await fetch_sheet(
                sheet_id=100, user_agent="agent", access_token="token"
            )
        assert mock_get.await_count == 3
        assert e.value.status_code == 503
        assert e.value.detail == "Service unavailable"

    @patch("httpx.AsyncClient.get")
    async def test_fetch_sheet_not_found(self, mock_get: AsyncMock):
        """Tests a non-retryable error is raised without retrying"""
        mock_get.return_value = httpx.Response(
            404, json={"errorCode": 1006, "message": "Not Found"}
        )
        with pytest.raises(HTTPException) as e:
            await fetch_sheet(
                sheet_id=100, user_agent="agent", access_token="token"
            )
        assert mock_get.await_count == 1
        assert e.value.status_code == 404
        assert e.value.detail == "Not Found"

    @patch("httpx.AsyncClient.get")
    async def test_fetch_sheet_error_not_json(self, mock_get: AsyncMock):
        """Tests a default message is used if the error body is not JSON"""
        mock_get.return_value = httpx.Response(401, content=b"<html>")
        with pytest.raises(HTTPException) as e:
            await fetch_sheet(
                sheet_id=100, user_agent="agent", access_token="token"
            )
        assert e.value.status_code == 401
        assert e.value.detail == "Smartsheet error"

    @patch("httpx.AsyncClient.get")
    async def test_fetch_sheet_transport_error(self, mock_get: AsyncMock):
        """Tests network errors are propagated"""
        mock_get.side_effect = httpx.ConnectError("Fail")
        with pytest.raises(httpx.ConnectError):
            await fetch_sheet(
                sheet_id=100, user_agent="agent", access_token="token"
            )
