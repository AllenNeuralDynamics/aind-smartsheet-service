"""Module to handle smartsheet api responses"""

from typing import Any, List, Optional, Type

from aind_smartsheet_api.client import SmartsheetClient
from pydantic import BaseModel

from aind_smartsheet_service_server.models import (
    FundingModel,
    PerfusionsModel,
    ProtocolsModel,
)


class SessionHandler:
    """Handle session object to get data"""

    def __init__(self, session: SmartsheetClient):
        """Class constructor"""
        self.session = session

    def get_parsed_sheet(
        self, sheet_id: int, model: Type[BaseModel]
    ) -> List[Any]:
        """
        Converts the rows in a Smart Sheet into a Pydantic model
        Parameters
        ----------
        sheet_id : int
          ID number of smart sheet
        model : Type[BaseModel]
          Pydantic model to parse the sheet to

        Returns
        -------
        List[Any]
          A list of Pydantic models

        """
        sheet = self.session.get_parsed_sheet_model(
            sheet_id=sheet_id, model=model, validate=False
        )
        return sheet

    @staticmethod
    def get_project_funding_info(
        sheet_model: List[FundingModel],
        project_name: Optional[str] = None,
        subproject: Optional[str] = None,
    ) -> List[FundingModel]:
        """
        Filters funding sheet by specific project name
        Parameters
        ----------
        sheet_model : List[FundingModel]
        project_name : str | None
        subproject : str | None

        Returns
        -------
        List[FundingModel]
          In the event that there are multiple project names, will return
          A list of all of that match the project name.

        """
        filtered_rows = [
            r
            for r in sheet_model
            if (
                r.project_name == project_name
                and (subproject is None or r.subproject == subproject)
            )
            or (project_name is None and subproject is None)
        ]
        return filtered_rows

    @staticmethod
    def get_project_names(sheet_model: List[FundingModel]) -> List[str]:
        """
        Returns a sorted list of unique project names found in the Funding
        SmartSheet.
        Parameters
        ----------
        sheet_model : List[FundingModel]

        Returns
        -------
        List[str]

        """
        project_names = set()
        for funding_model in sheet_model:
            project_name = funding_model.project_name
            subproject_name = funding_model.subproject
            if project_name is not None and subproject_name is None:
                project_names.add(project_name)
            elif project_name is not None and subproject_name is not None:
                project_names.add(f"{project_name} - {subproject_name}")
        sorted_names = sorted(list(set(project_names)))
        return sorted_names

    @staticmethod
    def get_protocols_info(
        sheet_model: List[ProtocolsModel], protocol_name: Optional[str] = None
    ) -> List[ProtocolsModel]:
        """
        Filter protocols Smartsheet by protocols name
        Parameters
        ----------
        sheet_model : List[ProtocolsModel]
        protocol_name : str | None

        Returns
        -------
        List[ProtocolsModel]
          In the event that there are multiple project names, will return
          A list of all of that match the project name.

        """
        filtered_rows = [
            r
            for r in sheet_model
            if r.protocol_name == protocol_name or protocol_name is None
        ]
        return filtered_rows

    @staticmethod
    def get_perfusions_info(
        sheet_model: List[PerfusionsModel], subject_id: Optional[str] = None
    ) -> List[PerfusionsModel]:
        """

        Parameters
        ----------
        sheet_model : List[PerfusionsModel]
        subject_id : str | None

        Returns
        -------
        List[PerfusionsModel]
          In the event that there are multiple project names, will return
          A list of all of that match the project name.
        """
        filtered_rows = [
            r
            for r in sheet_model
            if str(int(r.subject_id)) == subject_id or subject_id is None
        ]
        return filtered_rows
