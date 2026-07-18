"""Tests configs module"""

import os
import unittest
from unittest.mock import patch

from pydantic import SecretStr

from aind_smartsheet_service_server.configs import Settings


class TestSettings(unittest.TestCase):
    """Test methods in Settings Class"""

    @patch.dict(
        os.environ,
        {
            "SMARTSHEET_ACCESS_TOKEN": "abcdef2",
            "SMARTSHEET_ACCESS_TOKEN_2": "uvwxyz3",
            "SMARTSHEET_FUNDING_ID": "100",
            "SMARTSHEET_PROTOCOLS_ID": "101",
            "SMARTSHEET_PERFUSIONS_ID": "102",
            "SMARTSHEET_MOUSE_TRACKER_ID": "103",
            "SMARTSHEET_SAMPLE_TRACKING_ID": "104",
            "SMARTSHEET_IMAGING_QUEUE_ID": "105",
            "SMARTSHEET_EXASPIM_QC_SHEET_ID": "106",
        },
        clear=True,
    )
    def test_get_settings(self):
        """Tests settings can be set via env vars"""
        settings = Settings()
        expected_settings = Settings(
            access_token=SecretStr("abcdef2"),
            access_token_2=SecretStr("uvwxyz3"),
            funding_id=100,
            protocols_id=101,
            perfusions_id=102,
            mouse_tracker_id=103,
            sample_tracking_id=104,
            imaging_queue_id=105,
            exaspim_qc_sheet_id=106,
        )
        self.assertEqual(expected_settings, settings)


if __name__ == "__main__":
    unittest.main()
