"""Module to handle smartsheet api responses"""

from typing import Any, Dict, List, Optional, Type, TypeVar

from pydantic import BaseModel, ValidationError

from aind_smartsheet_service_server.models import (
    FundingModel,
    PerfusionsModel,
    ProtocolsModel,
    SheetFields,
    SheetRow,
)

T = TypeVar("T", bound=BaseModel)


class SessionHandler:
    """Handle session object to get data"""

    def __init__(self, raw_sheet: str):
        """Class constructor"""
        self.raw_sheet = raw_sheet

    def get_sheet_fields(self) -> SheetFields:
        """
        Returns
        -------
        SheetFields

        """
        return SheetFields.model_validate_json(self.raw_sheet)

    @staticmethod
    def _column_id_map(sheet_fields: SheetFields) -> Dict[int, str]:
        """
        SmartSheet uses integer ids for the columns. We need a way to
        map the column titles to the ids so we can retrieve information using
        just the titles.
        Parameters
        ----------
        sheet_fields : SheetFields

        Returns
        -------
        Dict[int, str]

        """
        return {c.id: c.title for c in sheet_fields.columns}

    @staticmethod
    def _map_row_to_dict(
        row: SheetRow, column_id_map: Dict[int, str]
    ) -> Dict[str, Any]:
        """
        Maps a row into a dictionary that maps the column names to their values
        Parameters
        ----------
        row : SheetRow
          A SheetRow that will be parsed. This a list of cells with a columnId
          and a cell value.
        column_id_map: Dict[int, str]
          Map of column ids into the column names

        Returns
        -------
        Dict[str, Any]
          The list of row cells is converted to a dictionary.

        """
        output_dict = {}
        for cell in row.cells:
            column_id = cell.columnId
            column_name = column_id_map[column_id]
            output_dict[column_name] = cell.value
        return output_dict

    def get_parsed_sheet(self) -> List[Dict[str, Any]]:
        """

        Returns
        -------
        List[Dict[str, Any]]

        """

        sheet_fields = self.get_sheet_fields()
        column_id_map = self._column_id_map(sheet_fields=sheet_fields)
        parsed_rows = list()
        for row in sheet_fields.rows:
            row_dict = self._map_row_to_dict(row, column_id_map=column_id_map)
            parsed_rows.append(row_dict)
        return parsed_rows

    def get_parsed_sheet_model(
        self, model: Type[T], validate: bool = True
    ) -> List[T]:
        """
        Parse raw sheet json into basic dictionary of {"name": "value"}
        Parameters
        ----------
        model : T
          BaseModel type
        validate : bool
          If set to True, will raise errors if pydantic validation fails.
          If set to False, will use model_construct in places where validation
          fails. Default is True.

        Returns
        -------
        List[T]

        """

        sheet_fields = self.get_sheet_fields()
        column_id_map = self._column_id_map(sheet_fields=sheet_fields)
        parsed_rows = list()
        for row in sheet_fields.rows:
            row_dict = self._map_row_to_dict(row, column_id_map=column_id_map)
            try:
                row_as_model = model.model_validate(row_dict)
                parsed_rows.append(row_as_model)

            except ValidationError as e:
                if validate:
                    raise e
                else:
                    row_as_model = model.model_construct(**row_dict)
                    parsed_rows.append(row_as_model)
        return parsed_rows

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
