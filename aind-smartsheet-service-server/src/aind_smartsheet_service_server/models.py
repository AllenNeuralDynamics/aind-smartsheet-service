"""Module for defining models from Smartsheet"""

from datetime import date as date_type
from datetime import datetime
from decimal import Decimal
from typing import Any, List, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, field_validator

from aind_smartsheet_service_server import __version__


class HealthCheck(BaseModel):
    """Response model to validate and return when performing a health check."""

    status: Literal["OK"] = "OK"
    service_version: str = __version__


def _parse_datetime_str(value: Any) -> datetime:
    """Adds handling of datetime strings that end with both offset and Z"""
    if isinstance(value, str) and value.endswith("+00:00Z"):
        return datetime.fromisoformat(value.replace("+00:00Z", "+00:00"))
    elif isinstance(value, str):
        return datetime.fromisoformat(value)
    else:
        return value


class SheetColumn(BaseModel):
    """SmartSheet column information"""

    id: int
    index: int
    title: str
    type: str
    validation: bool
    version: int
    width: int
    options: List[str] = []
    primary: bool = False
    hidden: Optional[bool] = None


class SheetRowCell(BaseModel):
    """SmartSheet 'row.cell' information"""

    columnId: int
    displayValue: Optional[str] = None
    value: Optional[Union[str, float]] = None


class SheetRow(BaseModel):
    """SmartSheet row information"""

    cells: List[SheetRowCell]
    createdAt: datetime
    expanded: bool
    id: int
    modifiedAt: datetime
    rowNumber: int
    siblingId: Optional[int] = None

    validate_fields = field_validator(
        "createdAt", "modifiedAt", mode="before"
    )(_parse_datetime_str)


class SheetFields(BaseModel):
    """SmartSheet information"""

    columns: List[SheetColumn]
    accessLevel: str
    createdAt: datetime
    dependenciesEnabled: bool
    effectiveAttachmentOptions: List[str]
    ganttEnabled: bool
    hasSummaryFields: bool
    id: int
    modifiedAt: datetime
    name: str
    permalink: str
    readOnly: bool
    resourceManagementEnabled: bool
    rows: List[SheetRow]
    totalRowCount: int
    userPermissions: dict
    userSettings: dict
    version: int
    workspace: dict = {}

    validate_fields = field_validator(
        "createdAt", "modifiedAt", mode="before"
    )(_parse_datetime_str)


class FundingModel(BaseModel):
    """Expected model for the Funding Sheet"""

    project_name: Optional[str] = Field(None, alias="Project Name")
    subproject: Optional[str] = Field(None, alias="Subproject")
    project_code: Optional[str] = Field(None, alias="Project Code")
    funding_institution: Optional[str] = Field(
        None, alias="Funding Institution"
    )
    grant_number: Optional[str] = Field(None, alias="Grant Number")
    fundees: Optional[str] = Field(None, alias="Fundees (PI)")
    investigators: Optional[str] = Field(None, alias="Investigators")
    model_config = ConfigDict(populate_by_name=True)


class PerfusionsModel(BaseModel):
    """Expected model for the Perfusions SmartSheet"""

    subject_id: Optional[Decimal] = Field(None, alias="subject id")
    date: Optional[date_type] = Field(None, alias="date")
    experimenter: Optional[str] = Field(None, alias="experimenter")
    iacuc_protocol: Optional[str] = Field(None, alias="iacuc protocol")
    animal_weight_prior: Optional[Decimal] = Field(
        None, alias="animal weight prior (g)"
    )
    output_specimen_id: Optional[Decimal] = Field(
        None, alias="Output specimen id(s)"
    )
    postfix_solution: Optional[str] = Field(None, alias="Postfix solution")
    notes: Optional[str] = Field(None, alias="Notes")
    model_config = ConfigDict(populate_by_name=True)


class ProtocolsModel(BaseModel):
    """Expected model for the Protocols SmartSheet"""

    protocol_type: Optional[str] = Field(None, alias="Protocol Type")
    procedure_name: Optional[str] = Field(None, alias="Procedure name")
    protocol_name: Optional[str] = Field(None, alias="Protocol name")
    doi: Optional[str] = Field(None, alias="DOI")
    version: Optional[Decimal] = Field(None, alias="Version")
    protocol_collection: Optional[bool] = Field(
        None, alias="Protocol collection"
    )
    model_config = ConfigDict(populate_by_name=True)
