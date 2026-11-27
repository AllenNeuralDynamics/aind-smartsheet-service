"""Module to test main app"""

from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient

from aind_smartsheet_service_server.configs import settings
from aind_smartsheet_service_server.route import EXASPIM_SHEETS


class TestMain:
    """Tests app endpoints"""

    def test_app_with_redis(self, client_with_redis: TestClient):
        """Tests client is instantiated correctly when redis_url set."""
        response = client_with_redis.get("/healthcheck")
        assert 200 == response.status_code

    def test_app_with_in_memory_cache(self, client: TestClient):
        """Tests client is instantiated correctly when redis_url None."""
        response = client.get("/healthcheck")
        assert 200 == response.status_code

    @patch(
        "aind_smartsheet_service_server.sheet_cache.SheetIndexCache"
        ".refresh_periodically",
        new_callable=AsyncMock,
    )
    def test_app_starts_cache_refresh(self, mock_refresh: AsyncMock):
        """Tests the exaSPIM sheets are refreshed in the background when
        cache_refresh_interval is set."""
        from aind_smartsheet_service_server.main import app

        with patch.object(settings, "cache_refresh_interval", 300):
            with TestClient(app) as c:
                response = c.get("/healthcheck")
        assert 200 == response.status_code
        mock_refresh.assert_awaited_once_with(
            sheets=[(s_id, c_id) for s_id, _, c_id in EXASPIM_SHEETS],
            interval=300,
        )


if __name__ == "__main__":
    pytest.main([__file__])
