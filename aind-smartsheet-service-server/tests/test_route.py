"""Test routes"""

from unittest.mock import AsyncMock, patch

import pytest
from fastapi_cache.backends.inmemory import InMemoryBackend
from starlette.testclient import TestClient

from aind_smartsheet_service_server.configs import settings
from aind_smartsheet_service_server.models import SheetFields
from aind_smartsheet_service_server.route import get_smartsheet


@pytest.mark.asyncio
class TestRoutes:
    """Test responses in route module."""

    async def test_get_health(self, client: TestClient):
        """Tests healthcheck route"""
        response = client.get("/healthcheck")
        assert 200 == response.status_code
        assert "OK" == response.json()["status"]

    @patch("aind_smartsheet_service_server.route.fetch_sheet")
    async def test_get_smartsheet(
        self, mock_fetch_sheet: AsyncMock, mock_raw_funding_sheet
    ):
        """Tests get_smartsheet returns the fetched sheet as a dict"""
        mock_fetch_sheet.return_value = mock_raw_funding_sheet
        sheet = await get_smartsheet(
            sheet_id=0,
            user_agent="user",
            access_token="token",
        )
        mock_fetch_sheet.assert_awaited_once_with(
            sheet_id=0, user_agent="user", access_token="token"
        )
        assert mock_raw_funding_sheet.version == sheet["version"]

    @patch("aind_smartsheet_service_server.route.get_smartsheet")
    async def test_get_funding(
        self,
        mock_get_sheet: AsyncMock,
        client: TestClient,
        mock_raw_funding_sheet: str,
    ):
        """Tests a good response when fetching funding info"""

        mock_get_sheet.return_value = mock_raw_funding_sheet
        project_name = (
            "Discovery-Neuromodulator circuit dynamics during foraging"
        )
        subproject = "Subproject 2 Molecular Anatomy Cell Types"
        response = client.get(
            f"/funding?project_name={project_name}&subproject={subproject}"
        )
        expected_response = [
            {
                "project_name": f"{project_name}",
                "subproject": f"{subproject}",
                "project_code": "122-01-001-10",
                "funding_institution": "Allen Institute",
                "grant_number": None,
                "fundees": (
                    "Person Four, Person Five, Person Six, Person Seven,"
                    " Person Eight"
                ),
                "investigators": "Person Seven",
            },
            {
                "project_name": f"{project_name}",
                "subproject": f"{subproject}",
                "project_code": "122-01-020-20",
                "funding_institution": "NIMH",
                "grant_number": "1R01MH134833",
                "fundees": (
                    "Person Five, Person Nine, Person Ten, Person Seven,"
                    " Person Eleven"
                ),
                "investigators": "Person Seven",
            },
        ]
        assert 200 == response.status_code
        assert expected_response == response.json()

    @patch("aind_smartsheet_service_server.route.get_smartsheet")
    async def test_get_project_names(
        self,
        mock_get_sheet: AsyncMock,
        client: TestClient,
        mock_raw_funding_sheet: str,
    ):
        """Tests a good response when fetching project_names"""

        mock_get_sheet.return_value = mock_raw_funding_sheet
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

        response = client.get("/project_names")
        expected_response = [
            f"{discovery_project} - {sub1}",
            f"{discovery_project} - {sub2}",
            f"{discovery_project} - {sub3}",
            "Ephys Platform",
            "MSMA Platform",
        ]
        assert 200 == response.status_code
        assert expected_response == response.json()

    @patch("aind_smartsheet_service_server.route.get_smartsheet")
    async def test_get_protocols(
        self,
        mock_get_sheet: AsyncMock,
        client: TestClient,
        mock_raw_protocols_sheet: str,
    ):
        """Tests a good response when fetching protocols"""

        mock_get_sheet.return_value = mock_raw_protocols_sheet
        example_protocol = (
            "Tetrahydrofuran and Dichloromethane Delipidation of a Whole "
            "Mouse Brain"
        )
        expected_response = [
            {
                "protocol_type": "Specimen Procedures",
                "procedure_name": "Delipidation",
                "protocol_name": f"{example_protocol}",
                "doi": "dx.doi.org/10.17504/protocols.io.36wgqj1kxvk5/v1",
                "version": "1",
                "protocol_collection": None,
                "website_pages": None,
            }
        ]
        response = client.get(f"/protocols?protocol_name={example_protocol}")
        assert 200 == response.status_code
        assert expected_response == response.json()

    @patch("aind_smartsheet_service_server.route.get_smartsheet")
    async def test_get_perfusions(
        self,
        mock_get_sheet: AsyncMock,
        client: TestClient,
        mock_raw_perfusions_sheet: str,
    ):
        """Tests a good response when fetching perfusions info"""

        mock_get_sheet.return_value = mock_raw_perfusions_sheet

        response = client.get("/perfusions?subject_id=689418")
        expected_response = [
            {
                "subject_id": "689418",
                "date": "2023-10-02",
                "experimenter": "Person S",
                "iacuc_protocol": (
                    "2109 - Analysis of brain - wide neural circuits in the"
                    " mouse"
                ),
                "animal_weight_prior": "22",
                "output_specimen_id": "689418",
                "postfix_solution": "1xPBS",
                "notes": "Good",
            }
        ]
        assert 200 == response.status_code
        assert expected_response == response.json()

    @patch("aind_smartsheet_service_server.sheet_cache.fetch_sheet")
    async def test_get_exaspim_info(
        self,
        mock_fetch_sheet: AsyncMock,
        client: TestClient,
        in_memory_cache: InMemoryBackend,
        mock_raw_mouse_tracking_sheet: SheetFields,
        mock_raw_sample_tracking_sheet: SheetFields,
        mock_raw_imaging_queue_sheet: SheetFields,
        mock_raw_qc_sheet: SheetFields,
    ):
        """Tests successful retrieval of info from exaSPIM Smartsheets"""
        sheets = {
            settings.mouse_tracker_id: mock_raw_mouse_tracking_sheet,
            settings.sample_tracking_id: mock_raw_sample_tracking_sheet,
            settings.imaging_queue_id: mock_raw_imaging_queue_sheet,
            settings.exaspim_qc_sheet_id: mock_raw_qc_sheet,
        }
        mock_fetch_sheet.side_effect = lambda sheet_id, **_: sheets[sheet_id]
        response = client.get("/get_exaspim_info?specimen_id=822178")
        assert response.status_code == 200
        assert len(response.json()["mouse_tracker_info"]) == 1
        assert len(response.json()["sample_tracking_info"]) == 1
        assert len(response.json()["imaging_queue_info"]) == 1
        assert len(response.json()["qc_sheet_info"]) == 1
        assert mock_fetch_sheet.await_count == 4

        # Second request is served from the cache
        response = client.get("/get_exaspim_info?specimen_id=000000")
        assert response.status_code == 200
        assert response.json() == {
            "mouse_tracker_info": [],
            "sample_tracking_info": [],
            "imaging_queue_info": [],
            "qc_sheet_info": [],
        }
        assert mock_fetch_sheet.await_count == 4


if __name__ == "__main__":
    pytest.main([__file__])
