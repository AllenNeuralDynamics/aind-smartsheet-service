"""Module for defining models from Smartsheet"""

from datetime import date as date_type
from datetime import datetime
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

    project_name: str | None = Field(
        default=None, title="Project Name", validation_alias="2802903489138564"
    )
    subproject: str | None = Field(
        default=None, title="Subproject", validation_alias="3987940745367428"
    )
    project_code: str | None = Field(
        default=None, title="Project Code", validation_alias="367734341717892"
    )
    funding_institution: str | None = Field(
        default=None,
        title="Funding Institution",
        validation_alias="7306503116509060",
    )
    grant_number: str | None = Field(
        default=None, title="Grant Number", validation_alias="8432403023351684"
    )
    fundees: str | None = Field(
        default=None, title="Fundees (PI)", validation_alias="1114053628874628"
    )
    investigators: str | None = Field(
        default=None,
        title="Investigators",
        validation_alias="5793496946659204",
    )
    model_config = ConfigDict(populate_by_name=True)


class PerfusionsModel(BaseModel):
    """Expected model for the Perfusions SmartSheet"""

    subject_id: str | None = Field(
        default=None, title="subject id", validation_alias="3203397935124356"
    )
    date: date_type | None = Field(
        default=None, title="date", validation_alias="7706997562494852"
    )
    experimenter: str | None = Field(
        default=None, title="experimenter", validation_alias="2077498028281732"
    )
    iacuc_protocol: str | None = Field(
        default=None,
        title="iacuc protocol",
        validation_alias="6581097655652228",
    )
    animal_weight_prior: str | None = Field(
        default=None,
        title="animal weight prior (g)",
        validation_alias="4329297841966980",
    )
    output_specimen_id: str | None = Field(
        default=None,
        title="Output specimen id(s)",
        validation_alias="8938618089328516",
    )
    postfix_solution: str | None = Field(
        default=None,
        title="Postfix solution",
        validation_alias="4554304736153476",
    )
    notes: str | None = Field(
        default=None, title="Notes", validation_alias="36971950854020"
    )
    model_config = ConfigDict(populate_by_name=True)


class ProtocolsModel(BaseModel):
    """Expected model for the Protocols SmartSheet"""

    protocol_type: str | None = Field(
        default=None,
        title="Protocol Type",
        validation_alias="8808571546324868",
    )
    procedure_name: str | None = Field(
        default=None,
        title="Procedure name",
        validation_alias="6725511871942532",
    )
    protocol_name: str | None = Field(
        default=None,
        title="Protocol name",
        validation_alias="6394619537346436",
    )
    doi: str | None = Field(
        default=None, title="DOI", validation_alias="4142819723661188"
    )
    version: str | None = Field(
        default=None, title="Version", validation_alias="8646419351031684"
    )
    protocol_collection: bool | None = Field(
        default=None,
        title="Protocol collection",
        validation_alias="223584756649860",
    )
    website_pages: str | None = Field(
        default=None, title="Website pages", validation_alias="388788696338308"
    )
    model_config = ConfigDict(populate_by_name=True)
