"""Module to handle smartsheet api responses"""

from collections.abc import Callable
from typing import Any, Dict, List, Optional, TypeVar

from pydantic import BaseModel, ValidationError

from aind_smartsheet_service_server.models import (
    SheetFields,
    SheetRow,
)

T = TypeVar("T", bound=BaseModel)


def default_row_map(
    row: SheetRow, by_display_value: bool = True
) -> Dict[str, Any]:
    """
    Maps a row into a dictionary like {"columnID": "displayValue"}
    Parameters
    ----------
    row : SheetRow
      A SheetRow that will be parsed. This has a list of cells with a columnId
      and a cell value.
    by_display_value : bool
      Whether to use the displayValue instead of the value. Default is True.

    Returns
    -------
    Dict[str, Any]

    """
    output_dict = {}
    for cell in row.cells:
        column_id = cell.columnId
        if by_display_value and cell.displayValue:
            output_dict[str(column_id)] = cell.displayValue
        else:
            output_dict[str(column_id)] = cell.value
    return output_dict


def default_row_filter(
    row: SheetRow,
    column_id: Optional[int],
    column_display_value: Optional[str],
) -> bool:
    """
    A default row filter that can be optionally attached to a handler.
    Parameters
    ----------
    row : SheetRow
    column_id : int | None
    column_display_value : str | None

    Returns
    -------
    bool
      True to keep the row and False to filter it out.

    """
    if column_id:
        for cell in row.cells:
            if (
                cell.columnId == column_id
                and cell.displayValue == column_display_value
            ):
                return True
        return False
    else:
        return True


class SheetHandler:
    """Handle raw sheet object"""

    def __init__(
        self,
        sheet_fields: SheetFields,
        validate: bool = True,
        row_filter: Callable[
            [SheetRow], bool
        ] = lambda row: default_row_filter(row, None, None),
        row_mapper: Callable[[SheetRow], dict] = lambda row: default_row_map(
            row, True
        ),
    ):
        """Class constructor"""
        self.sheet_fields = sheet_fields
        self.validate = validate
        self.row_filter = row_filter
        self.row_mapper = row_mapper

    def get_parsed_sheet_model(self, model: type[T]) -> List[T]:
        """
        Parse raw sheet json into basic dictionary of {"name": "value"}
        Parameters
        ----------
        model : T
          BaseModel type

        Returns
        -------
        List[T]

        """
        matched_rows = [
            row for row in self.sheet_fields.rows if self.row_filter(row)
        ]
        mapped_rows = [self.row_mapper(row) for row in matched_rows]
        parsed_rows = []
        for row in mapped_rows:
            try:
                mapped_row = model.model_validate(row)
            except ValidationError as e:
                if self.validate:
                    raise e
                mapped_row = model.model_construct(**row)
            parsed_rows.append(mapped_row)
        return parsed_rows
