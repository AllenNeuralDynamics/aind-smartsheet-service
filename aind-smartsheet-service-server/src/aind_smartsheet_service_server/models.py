"""Module for defining models from Smartsheet"""

from datetime import date as date_type
from decimal import Decimal
from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, Field

from aind_smartsheet_service_server import __version__


class HealthCheck(BaseModel):
    """Response model to validate and return when performing a health check."""

    status: Literal["OK"] = "OK"
    service_version: str = __version__


class FundingModel(BaseModel):
    """Expected model for the Funding Sheet"""

    project_name: Optional[str] = Field(None, alias="Project Name")
    subproject: Optional[str] = Field(None, alias="Subproject")
    project_code: Optional[str] = Field(None, alias="Project Code")
    funding_institution: Optional[str] = Field(
        None, alias="Funding Institution"
    )
    grant_number: Optional[str] = Field(None, alias="Grant Number")
    fundees: Optional[str] = Field(None, alias="Fundees")
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
