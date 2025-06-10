"""Tests session module"""

import pytest

from aind_smartsheet_service_server.session import get_session


class TestSession:
    """Test methods in Session Class"""

    def test_get_session(self):
        """Tests get_session method"""

        session = next(get_session())
        assert (
            "abcdef"
            == session.smartsheet_settings.access_token.get_secret_value()
        )


if __name__ == "__main__":
    pytest.main([__file__])
