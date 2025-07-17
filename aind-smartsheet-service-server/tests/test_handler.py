"""Tests handler module"""

import json
import os
import unittest
from datetime import date
from decimal import Decimal
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, ValidationError

from aind_smartsheet_service_server.handler import SheetHandler
from aind_smartsheet_service_server.models import (
    FundingModel,
    PerfusionsModel,
    ProtocolsModel,
)

RESOURCES_DIR = Path(os.path.dirname(os.path.realpath(__file__))) / "resources"


class TestSessionHandler(unittest.TestCase):
    """Test methods in SessionHandler Class"""

    class MockSheetModel1(BaseModel):
        """Mocked class to hold sheet model with all valid fields for mocked
        sheet contents"""

        project_name: Optional[str] = Field(None, alias="Project Name")
        project_code: str = Field(..., alias="Project Code")
        funding_institution: str = Field(..., alias="Funding Institution")
        grant_number: Optional[str] = Field(None, alias="Grant Number")
        investigators: str = Field(..., alias="Investigators")
        model_config = ConfigDict(populate_by_name=True)

    class MockSheetModel2(BaseModel):
        """Mocked class to hold sheet model with some invalid fields for
        mocked sheet contents"""

        project_name: str = Field(..., alias="Project Name")
        project_code: str = Field(..., alias="Project Code")
        funding_institution: str = Field(..., alias="Funding Institution")
        # Some grant numbers are None, so this will be invalid
        grant_number: str = Field(..., alias="Grant Number")
        investigators: str = Field(..., alias="Investigators")
        model_config = ConfigDict(populate_by_name=True)

    @classmethod
    def setUpClass(cls) -> None:
        """Set up class with loaded json and shared examples."""

        with open(RESOURCES_DIR / "funding.json", "r") as f:
            funding_response = json.load(f)

        with open(RESOURCES_DIR / "perfusions.json", "r") as f:
            perfusions_response = json.load(f)

        with open(RESOURCES_DIR / "protocols.json", "r") as f:
            protocols_response = json.load(f)

        with open(RESOURCES_DIR / "example_sheet.json", "r") as f:
            example_sheet_response = json.load(f)

        cls.funding_response = json.dumps(funding_response)
        cls.perfusions_response = json.dumps(perfusions_response)
        cls.protocols_response = json.dumps(protocols_response)
        cls.example_sheet_response = json.dumps(example_sheet_response)

        discovery_project = (
            "Discovery-Neuromodulator circuit dynamics during foraging"
        )
        sub1 = (
            "Subproject 1 Electrophysiological Recordings from NM Neurons"
            " During Behavior"
        )
        sub2 = "Subproject 2 Molecular Anatomy Cell Types"
        sub3 = (
            "Subproject 3 Fiber Photometry Recordings of NM Release"
            " During Behavior"
        )

        cls.expected_funding_sheet = [
            FundingModel(),
            FundingModel(
                project_name="Ephys Platform",
                funding_institution="Allen Institute",
                fundees="Person One, Person Two, Person Three",
            ),
            FundingModel(
                project_name="MSMA Platform",
                project_code="122-01-001-10",
                funding_institution="Allen Institute",
                fundees="Person Four",
            ),
            FundingModel(
                project_name=discovery_project,
                subproject=sub1,
                project_code="122-01-001-10",
                funding_institution="Allen Institute",
                fundees=(
                    "Person Four, Person Five, Person Six, Person Seven,"
                    " Person Eight"
                ),
            ),
            FundingModel(
                project_name=discovery_project,
                subproject=sub1,
                project_code="122-01-012-20",
                funding_institution="NINDS",
                grant_number="1RF1NS131984",
                fundees="Person Five, Person Six, Person Eight",
                investigators="Person Six, Person Eight",
            ),
            FundingModel(
                project_name=discovery_project,
                subproject=sub2,
                project_code="122-01-001-10",
                funding_institution="Allen Institute",
                grant_number=None,
                fundees=(
                    "Person Four, Person Five, Person Six, Person Seven,"
                    " Person Eight"
                ),
                investigators="Person Seven",
            ),
            FundingModel(
                project_name=discovery_project,
                subproject=sub2,
                project_code="122-01-020-20",
                funding_institution="NIMH",
                grant_number="1R01MH134833",
                fundees=(
                    "Person Five, Person Nine, Person Ten, Person Seven,"
                    " Person Eleven"
                ),
                investigators="Person Seven",
            ),
            FundingModel(
                project_name=discovery_project,
                subproject=sub3,
                project_code="122-01-001-10",
                funding_institution="Allen Institute",
                fundees=(
                    "Person Four, Person Five, Person Six, Person Seven,"
                    " Person Eight"
                ),
                investigators=(
                    "Person Four, Person Ten, person.twelve@example.com,"
                    " person.thirteen@example.com, Person Eight"
                ),
            ),
            FundingModel(
                project_name=discovery_project,
                subproject=sub3,
                project_code="122-01-020-20",
                funding_institution="NIMH",
                grant_number="1R01MH134833",
                fundees=(
                    "Person Five, Person Nine, Person Ten, Person Seven,"
                    " Person Eleven"
                ),
                investigators=(
                    "Person Four, Person Ten, person.twelve@example.com,"
                    " person.thirteen@example.com, Person Eight"
                ),
            ),
        ]

        cls.expected_perfusions_sheet = [
            PerfusionsModel(
                subject_id=Decimal("689418.0"),
                date=date(2023, 10, 2),
                experimenter="Person S",
                iacuc_protocol=(
                    "2109 - Analysis of brain - wide neural circuits in the"
                    " mouse"
                ),
                animal_weight_prior=Decimal("22.0"),
                output_specimen_id=Decimal("689418.0"),
                postfix_solution="1xPBS",
                notes="Good",
            )
        ]
        cls.expected_protocols_sheet = [
            ProtocolsModel(
                protocol_type="Specimen Procedures",
                procedure_name="Immunolabeling",
                protocol_name="Immunolabeling of a Whole Mouse Brain",
                doi="dx.doi.org/10.17504/protocols.io.ewov1okwylr2/v1",
                version=Decimal("1.0"),
            ),
            ProtocolsModel(
                protocol_type="Specimen Procedures",
                procedure_name="Delipidation",
                protocol_name=(
                    "Tetrahydrofuran and Dichloromethane Delipidation of a "
                    "Whole Mouse Brain"
                ),
                doi="dx.doi.org/10.17504/protocols.io.36wgqj1kxvk5/v1",
                version=Decimal("1.0"),
            ),
            ProtocolsModel(
                protocol_type="Specimen Procedures",
                procedure_name="Delipidation",
                protocol_name=(
                    "Aqueous (SBiP) Delipidation of a Whole Mouse Brain"
                ),
                doi="dx.doi.org/10.17504/protocols.io.n2bvj81mwgk5/v1",
                version=Decimal("1.0"),
            ),
            ProtocolsModel(
                protocol_type="Specimen Procedures",
                procedure_name="Gelation + previous steps",
                protocol_name=(
                    "Whole Mouse Brain Delipidation, Immunolabeling, and "
                    "Expansion Microscopy"
                ),
                doi="dx.doi.org/10.17504/protocols.io.n92ldpwjxl5b/v1",
                version=Decimal("1.0"),
                protocol_collection=False,
            ),
            ProtocolsModel(
                protocol_type="Surgical Procedures",
                procedure_name="Injection Nanoject",
                protocol_name="Injection of Viral Tracers by Nanoject V.4",
                doi="dx.doi.org/10.17504/protocols.io.bp2l6nr7kgqe/v4",
                version=Decimal("4.0"),
            ),
            ProtocolsModel(
                protocol_type="Surgical Procedures",
                procedure_name="Injection Iontophoresis",
                protocol_name=(
                    "Stereotaxic Surgery for Delivery of Tracers by "
                    "Iontophoresis V.3"
                ),
                doi="dx.doi.org/10.17504/protocols.io.bgpvjvn6",
                version=Decimal("3.0"),
            ),
            ProtocolsModel(
                protocol_type="Surgical Procedures",
                procedure_name="Perfusion",
                protocol_name=(
                    "Mouse Cardiac Perfusion Fixation and Brain "
                    "Collection V.5"
                ),
                doi="dx.doi.org/10.17504/protocols.io.bg5vjy66",
                version=Decimal("5.0"),
            ),
            ProtocolsModel(
                protocol_type="Imaging Techniques",
                procedure_name="SmartSPIM Imaging",
                protocol_name="Imaging cleared mouse brains on SmartSPIM",
                doi="dx.doi.org/10.17504/protocols.io.3byl4jo1rlo5/v1",
                version=Decimal("1.0"),
            ),
            ProtocolsModel(
                protocol_type="Imaging Techniques",
                procedure_name="SmartSPIM setup",
                protocol_name="SmartSPIM setup and alignment",
                doi="dx.doi.org/10.17504/protocols.io.5jyl8jyb7g2w/v1",
                version=Decimal("1.0"),
            ),
            ProtocolsModel(),
            ProtocolsModel(),
            ProtocolsModel(),
            ProtocolsModel(),
        ]

    def test_column_id_map(self):
        """Tests _column_id_map method"""

        handler = SheetHandler(raw_sheet=self.example_sheet_response)
        sheet_fields = handler._get_sheet_fields()
        col_id_map = handler._column_id_map(sheet_fields=sheet_fields)
        expected_col_id_map = {
            3981351074090884: "Project Name",
            1729551260405636: "Project Code",
            2990791841501060: "Funding Institution",
            3446515788894084: "Grant Number",
            4825776004222852: "Investigators",
        }
        self.assertEqual(expected_col_id_map, col_id_map)

    def test_map_row_to_dict(self):
        """Tests _map_row_to_dict method"""

        handler = SheetHandler(raw_sheet=self.example_sheet_response)
        sheet_fields = handler._get_sheet_fields()
        col_id_map = handler._column_id_map(sheet_fields=sheet_fields)
        first_row = sheet_fields.rows[0]
        row_as_dict = handler._map_row_to_dict(
            row=first_row, column_id_map=col_id_map
        )
        expected_row_as_dict = {
            "Project Name": "AIND Scientific Activities",
            "Project Code": "122-01-001-10",
            "Funding Institution": "Allen Institute",
            "Grant Number": None,
            "Investigators": "person.two@acme.org, J Smith, John Doe II",
        }
        self.assertEqual(expected_row_as_dict, row_as_dict)

    def test_get_parsed_sheet_model_case_1(self):
        """Tests get_parsed_sheet_model method with validate set to True and
        no validation errors"""

        handler = SheetHandler(raw_sheet=self.example_sheet_response)
        parsed_sheet = handler._get_parsed_sheet_model(
            model=self.MockSheetModel1
        )
        expected_output = [
            self.MockSheetModel1(
                project_name="AIND Scientific Activities",
                project_code="122-01-001-10",
                funding_institution="Allen Institute",
                grant_number=None,
                investigators="person.two@acme.org, J Smith, John Doe II",
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

        handler = SheetHandler(raw_sheet=self.example_sheet_response)
        with self.assertRaises(ValidationError):
            handler._get_parsed_sheet_model(model=self.MockSheetModel2)

    def test_get_parsed_sheet_model_case_3(self):
        """Tests get_parsed_sheet_model method with validate set to False and
        validation errors"""

        handler = SheetHandler(
            raw_sheet=self.example_sheet_response, validate=False
        )
        parsed_sheet = handler._get_parsed_sheet_model(
            model=self.MockSheetModel2
        )
        expected_output = [
            self.MockSheetModel2.model_construct(
                project_name="AIND Scientific Activities",
                project_code="122-01-001-10",
                funding_institution="Allen Institute",
                grant_number=None,
                investigators="person.two@acme.org, J Smith, John Doe II",
            ),
            self.MockSheetModel2.model_construct(
                project_name=None,
                project_code="122-01-001-10",
                funding_institution="Allen Institute",
                grant_number=None,
                investigators="John Doe, person.one@acme.org",
            ),
            self.MockSheetModel2.model_construct(
                project_name="v1omFISH",
                project_code="121-01-010-10",
                funding_institution="Allen Institute",
                grant_number=None,
                investigators="person.one@acme.org, Jane Doe",
            ),
        ]
        self.assertEqual(expected_output, parsed_sheet)

    def test_get_protocols_info(self):
        """Tests get_protocols_info method"""
        handler = SheetHandler(raw_sheet=self.protocols_response)

        parsed_sheet = handler.get_protocols_info()
        self.assertEqual(self.expected_protocols_sheet, parsed_sheet)

    def test_get_perfusions_sheet(self):
        """Tests get_perfusions_info method"""
        handler = SheetHandler(raw_sheet=self.perfusions_response)

        parsed_sheet = handler.get_perfusions_info()
        self.assertEqual(self.expected_perfusions_sheet, parsed_sheet)

    def test_get_project_funding_info(self):
        """Tests get_project_funding_info method"""
        handler = SheetHandler(raw_sheet=self.funding_response)

        parsed_sheet = handler.get_project_funding_info()
        self.assertEqual(self.expected_funding_sheet, parsed_sheet)

    def test_get_project_funding_info_match(self):
        """Tests get_project_funding_info match"""
        handler = SheetHandler(raw_sheet=self.funding_response)
        funding_info = handler.get_project_funding_info(
            project_name="MSMA Platform"
        )
        self.assertEqual(self.expected_funding_sheet[2:3], funding_info)

    def test_get_project_funding_info_no_match(self):
        """Tests get_project_funding_info when no match"""

        handler = SheetHandler(raw_sheet=self.funding_response)
        funding_info = handler.get_project_funding_info(
            project_name="FAKE PROJECT"
        )
        self.assertEqual([], funding_info)

    def test_get_project_names(self):
        """Tests get_project_names"""

        handler = SheetHandler(raw_sheet=self.funding_response)
        project_names = handler.get_project_names()
        expected_names = [
            (
                "Discovery-Neuromodulator circuit dynamics during foraging"
                " - Subproject 1 Electrophysiological Recordings from NM "
                "Neurons During Behavior"
            ),
            (
                "Discovery-Neuromodulator circuit dynamics during foraging"
                " - Subproject 2 Molecular Anatomy Cell Types"
            ),
            (
                "Discovery-Neuromodulator circuit dynamics during foraging"
                " - Subproject 3 Fiber Photometry Recordings of NM Release"
                " During Behavior"
            ),
            "Ephys Platform",
            "MSMA Platform",
        ]
        self.assertEqual(expected_names, project_names)


if __name__ == "__main__":
    unittest.main()
