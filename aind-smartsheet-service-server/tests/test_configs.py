"""Tests configs module"""

import os
import unittest
from unittest.mock import patch

from aind_smartsheet_service_server.configs import Settings


class TestSettings(unittest.TestCase):
    """Test methods in Settings Class"""

    @patch.dict(
        os.environ,
        {
            "SMARTSHEET_ACCESS_TOKEN": "abcdef",
            "SMARTSHEET_FUNDING_ID": "123",
            "SMARTSHEET_PROTOCOLS_ID": "456",
            "SMARTSHEET_PERFUSIONS_ID": "789",
        },
        clear=True,
    )
    def test_get_settings(self):
        """Tests settings can be set via env vars"""
        settings = Settings()
        expected_settings = Settings(
            access_token="abcdef",
            funding_id=123,
            protocols_id=456,
            perfusions_id=789,
        )
        self.assertEqual(expected_settings, settings)


if __name__ == "__main__":
    unittest.main()
