"""Tests sheet_cache module"""

import asyncio
from unittest.mock import AsyncMock, patch

import httpx
import pytest
from fastapi import HTTPException
from fastapi_cache.backends.inmemory import InMemoryBackend

from aind_smartsheet_service_server.models import SheetFields
from aind_smartsheet_service_server.sheet_cache import (
    SheetIndexCache,
    build_index,
    fetch_sheet,
)
from tests.conftest import RESOURCES_DIR

# Specimen id column in the perfusions sheet
SUBJECT_COLUMN = 3203397935124356


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


class TestBuildIndex:
    """Tests build_index"""

    def test_build_index(self, mock_raw_perfusions_sheet: SheetFields):
        """Tests rows are grouped by the display value of a column"""
        index = build_index(mock_raw_perfusions_sheet, SUBJECT_COLUMN)
        rows = index["689418"]
        assert len(rows) == 1
        assert rows[0][str(SUBJECT_COLUMN)] == "689418"
        indexed_rows = sum(len(v) for v in index.values())
        rows_with_id = [
            r
            for r in mock_raw_perfusions_sheet.rows
            if any(
                c.columnId == SUBJECT_COLUMN and c.displayValue is not None
                for c in r.cells
            )
        ]
        assert indexed_rows == len(rows_with_id)

    def test_build_index_missing_column(
        self, mock_raw_perfusions_sheet: SheetFields
    ):
        """Tests an empty index when no rows have the column"""
        assert build_index(mock_raw_perfusions_sheet, 1) == {}


@pytest.fixture()
def index_cache(in_memory_cache: InMemoryBackend) -> SheetIndexCache:
    """SheetIndexCache backed by a fresh in-memory cache."""
    return SheetIndexCache(
        access_token="token",
        user_agent="agent",
        semaphore=asyncio.Semaphore(2),
    )


class TestSheetIndexCache:
    """Tests SheetIndexCache"""

    @patch("aind_smartsheet_service_server.sheet_cache.fetch_sheet")
    async def test_get_caches_index(
        self,
        mock_fetch_sheet: AsyncMock,
        index_cache: SheetIndexCache,
        in_memory_cache: InMemoryBackend,
        mock_raw_perfusions_sheet: SheetFields,
    ):
        """Tests the sheet is downloaded once and then read from the cache"""
        mock_fetch_sheet.return_value = mock_raw_perfusions_sheet
        first = await index_cache.get(102, SUBJECT_COLUMN)
        second = await index_cache.get(102, SUBJECT_COLUMN)
        assert first == second
        assert "689418" in first
        mock_fetch_sheet.assert_awaited_once_with(
            sheet_id=102, user_agent="agent", access_token="token"
        )
        assert list(in_memory_cache._store) == [
            f"test:index:102:{SUBJECT_COLUMN}"
        ]

    @patch("aind_smartsheet_service_server.sheet_cache.fetch_sheet")
    async def test_get_concurrent_misses_download_once(
        self,
        mock_fetch_sheet: AsyncMock,
        index_cache: SheetIndexCache,
        mock_raw_perfusions_sheet: SheetFields,
    ):
        """Tests concurrent cache misses share a single download"""

        async def slow_fetch(**_):
            """Simulate a slow download"""
            await asyncio.sleep(0.05)
            return mock_raw_perfusions_sheet

        mock_fetch_sheet.side_effect = slow_fetch
        results = await asyncio.gather(
            *[index_cache.get(102, SUBJECT_COLUMN) for _ in range(5)]
        )
        assert all(r == results[0] for r in results)
        assert mock_fetch_sheet.await_count == 1

    @patch("aind_smartsheet_service_server.sheet_cache.fetch_sheet")
    async def test_get_refresh(
        self,
        mock_fetch_sheet: AsyncMock,
        index_cache: SheetIndexCache,
        mock_raw_perfusions_sheet: SheetFields,
    ):
        """Tests refresh downloads the sheet even when it is cached"""
        mock_fetch_sheet.return_value = mock_raw_perfusions_sheet
        await index_cache.get(102, SUBJECT_COLUMN)
        await index_cache.get(102, SUBJECT_COLUMN, refresh=True)
        assert mock_fetch_sheet.await_count == 2

    @patch("aind_smartsheet_service_server.sheet_cache.fetch_sheet")
    async def test_get_error_not_cached(
        self,
        mock_fetch_sheet: AsyncMock,
        index_cache: SheetIndexCache,
        in_memory_cache: InMemoryBackend,
    ):
        """Tests a failed download raises and does not cache anything"""
        mock_fetch_sheet.side_effect = HTTPException(status_code=404)
        with pytest.raises(HTTPException):
            await index_cache.get(102, SUBJECT_COLUMN)
        assert in_memory_cache._store == {}
