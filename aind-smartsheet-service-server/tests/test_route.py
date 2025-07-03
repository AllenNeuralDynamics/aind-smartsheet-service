"""Test routes"""

from unittest.mock import MagicMock

import pytest
from starlette.testclient import TestClient


class TestRoutes:
    """Test responses in route module."""

    def test_get_health(self, client: TestClient):
        """Tests healthcheck route"""
        response = client.get("/healthcheck")
        assert 200 == response.status_code
        assert "OK" == response.json()["status"]

    def test_get_200_funding(
        self, client: TestClient, mock_get_raw_funding_sheet: MagicMock
    ):
        """Tests a good response when fetching funding info"""
        project_name = (
            "Discovery-Neuromodulator circuit dynamics during foraging"
        )
        subproject = "Subproject 2 Molecular Anatomy Cell Types"
        response = client.get(
            f"/funding?project_name={project_name}&subproject={subproject}"
        )
        expected_response = [
            {
                "Project Name": f"{project_name}",
                "Subproject": f"{subproject}",
                "Project Code": "122-01-001-10",
                "Funding Institution": "Allen Institute",
                "Grant Number": None,
                "Fundees": (
                    "Person Four, Person Five, Person Six, Person Seven,"
                    " Person Eight"
                ),
                "Investigators": "Person Seven",
            },
            {
                "Project Name": f"{project_name}",
                "Subproject": f"{subproject}",
                "Project Code": "122-01-020-20",
                "Funding Institution": "NIMH",
                "Grant Number": "1R01MH134833",
                "Fundees": (
                    "Person Five, Person Nine, Person Ten, Person Seven,"
                    " Person Eleven"
                ),
                "Investigators": "Person Seven",
            },
        ]
        assert 200 == response.status_code
        assert expected_response == response.json()

    def test_get_200_project_names(
        self, client: TestClient, mock_get_raw_funding_sheet: MagicMock
    ):
        """Tests a good response when fetching project_names"""
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

    def test_get_200_protocols(
        self, client: TestClient, mock_get_raw_protocols_sheet: MagicMock
    ):
        """Tests a good response when fetching protocols"""

        example_protocol = (
            "Tetrahydrofuran and Dichloromethane Delipidation of a Whole "
            "Mouse Brain"
        )
        expected_response = [
            {
                "Protocol Type": "Specimen Procedures",
                "Procedure name": "Delipidation",
                "Protocol name": f"{example_protocol}",
                "DOI": "dx.doi.org/10.17504/protocols.io.36wgqj1kxvk5/v1",
                "Version": "1.0",
                "Protocol collection": None,
            }
        ]
        response = client.get(f"/protocols?protocol_name={example_protocol}")
        assert 200 == response.status_code
        assert expected_response == response.json()

    def test_get_200_perfusions(
        self, client: TestClient, mock_get_raw_perfusions_sheet: MagicMock
    ):
        """Tests a good response when fetching perfusions info"""

        response = client.get("/perfusions?subject_id=689418")
        expected_response = [
            {
                "subject id": "689418.0",
                "date": "2023-10-02",
                "experimenter": "Person S",
                "iacuc protocol": (
                    "2109 - Analysis of brain - wide neural circuits in the"
                    " mouse"
                ),
                "animal weight prior (g)": "22.0",
                "Output specimen id(s)": "689418.0",
                "Postfix solution": "1xPBS",
                "Notes": "Good",
            }
        ]
        assert 200 == response.status_code
        assert expected_response == response.json()


if __name__ == "__main__":
    pytest.main([__file__])
