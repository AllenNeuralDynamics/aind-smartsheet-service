"""Tests handler module"""

import json
import os
import unittest
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, ValidationError

from aind_smartsheet_service_server.handler import (
    SheetHandler,
    default_row_filter,
    default_row_map,
)
from aind_smartsheet_service_server.models import (
    SheetFields,
)

RESOURCES_DIR = Path(os.path.dirname(os.path.realpath(__file__))) / "resources"


class TestSessionHandler(unittest.TestCase):
    """Test methods in SessionHandler Class"""

    class MockSheetModel1(BaseModel):
        """Mocked class to hold sheet model with all valid fields for mocked
        sheet contents"""

        project_name: Optional[str] = Field(
            None, title="Project Name", validation_alias="3981351074090884"
        )
        project_code: str = Field(
            ..., title="Project Code", validation_alias="1729551260405636"
        )
        funding_institution: str = Field(
            ...,
            title="Funding Institution",
            validation_alias="2990791841501060",
        )
        grant_number: Optional[str] = Field(
            None, title="Grant Number", validation_alias="3446515788894084"
        )
        investigators: str = Field(
            ..., title="Investigators", validation_alias="4825776004222852"
        )
        model_config = ConfigDict(populate_by_name=True)

    class MockSheetModel2(MockSheetModel1):
        """Mocked class to hold sheet model with some invalid fields for
        mocked sheet contents"""

        # Some grant numbers are None, so this will be invalid
        grant_number: str = Field(..., alias="Grant Number")

    @classmethod
    def setUpClass(cls) -> None:
        """Set up class with loaded json and shared examples."""

        with open(RESOURCES_DIR / "example_sheet.json", "r") as f:
            example_sheet_response = json.load(f)

        cls.example_sheet_response = SheetFields.model_validate(
            example_sheet_response
        )

    def test_default_row_map(self):
        """Tests default_row_map method"""

        mapped_row = default_row_map(row=self.example_sheet_response.rows[0])
        expected_mapped_row = {
            "3981351074090884": "AIND Scientific Activities",
            "1729551260405636": "122-01-001-10",
            "2990791841501060": "Allen Institute",
            "3446515788894084": None,
            "4825776004222852": "person.two@acme.org, J Smith, Mary Smith",
        }
        self.assertEqual(expected_mapped_row, mapped_row)

    def test_default_row_map_by_display_value_false(self):
        """Tests default_row_map method when by_display_value is False"""

        mapped_row = default_row_map(
            row=self.example_sheet_response.rows[0], by_display_value=False
        )
        expected_mapped_row = {
            "3981351074090884": "AIND Scientific Activities",
            "1729551260405636": "122-01-001-10",
            "2990791841501060": "Allen Institute",
            "3446515788894084": None,
            "4825776004222852": "person.two@acme.org, J Smith, Mary Smith",
        }
        self.assertEqual(expected_mapped_row, mapped_row)

    def test_default_row_filter_no_col_id(self):
        """Tests default_row_filter method with no column_id provided."""
        self.assertTrue(
            default_row_filter(
                row=self.example_sheet_response.rows[0],
                column_id=None,
                column_display_value=None,
            )
        )

    def test_default_row_filter_match_found(self):
        """Tests default_row_filter returns True if match is found."""
        self.assertTrue(
            default_row_filter(
                row=self.example_sheet_response.rows[0],
                column_id=2990791841501060,
                column_display_value="Allen Institute",
            )
        )

    def test_default_row_filter_match_not_found(self):
        """Tests default_row_filter returns False if match is not found."""
        self.assertFalse(
            default_row_filter(
                row=self.example_sheet_response.rows[0],
                column_id=2990791841501060,
                column_display_value="ABC",
            )
        )

    def test_get_parsed_sheet_model_case_1(self):
        """Tests get_parsed_sheet_model method with validate set to True and
        no validation errors"""
        handler = SheetHandler(sheet_fields=self.example_sheet_response)
        parsed_sheet = handler.get_parsed_sheet_model(
            model=self.MockSheetModel1
        )
        expected_output = [
            self.MockSheetModel1(
                project_name="AIND Scientific Activities",
                project_code="122-01-001-10",
                funding_institution="Allen Institute",
                grant_number=None,
                investigators="person.two@acme.org, J Smith, Mary Smith",
            ),
            self.MockSheetModel1(
                project_name=None,
                project_code="122-01-001-10",
                funding_institution="Allen Institute",
                grant_number=None,
                investigators="John Doe, person.one@acme.org",
            ),
            self.MockSheetModel1(
                project_name="v1omFISH",
                project_code="121-01-010-10",
                funding_institution="Allen Institute",
                grant_number=None,
                investigators="person.one@acme.org, Jane Doe",
            ),
        ]
        self.assertEqual(expected_output, parsed_sheet)

    def test_get_parsed_sheet_model_case_2(self):
        """Tests get_parsed_sheet_model method with validate set to True and
        validation errors"""

        handler = SheetHandler(
            sheet_fields=self.example_sheet_response, validate=True
        )
        with self.assertRaises(ValidationError):
            handler.get_parsed_sheet_model(model=self.MockSheetModel2)

    def test_get_parsed_sheet_model_case_3(self):
        """Tests get_parsed_sheet_model method with validate set to False and
        validation errors"""

        handler = SheetHandler(
            sheet_fields=self.example_sheet_response, validate=False
        )
        parsed_sheet = handler.get_parsed_sheet_model(
            model=self.MockSheetModel2
        )
        expected_output = [
            self.MockSheetModel2.model_construct(
                project_name="AIND Scientific Activities",
                project_code="122-01-001-10",
                funding_institution="Allen Institute",
                investigators="person.two@acme.org, J Smith, Mary Smith",
            ),
            self.MockSheetModel2.model_construct(
                project_name=None,
                project_code="122-01-001-10",
                funding_institution="Allen Institute",
                investigators="John Doe, person.one@acme.org",
            ),
            self.MockSheetModel2.model_construct(
                project_name="v1omFISH",
                project_code="121-01-010-10",
                funding_institution="Allen Institute",
                investigators="person.one@acme.org, Jane Doe",
            ),
        ]
        self.assertEqual(expected_output, parsed_sheet)


if __name__ == "__main__":
    unittest.main()
