"""Module to handle endpoint responses"""

from asyncio import to_thread
from typing import List, Optional

from fastapi import APIRouter, Depends, Query, status
from fastapi_cache.decorator import cache
from smartsheet import Smartsheet

from aind_smartsheet_service_server.configs import Settings, get_settings
from aind_smartsheet_service_server.handler import SheetHandler
from aind_smartsheet_service_server.models import (
    FundingModel,
    HealthCheck,
    PerfusionsModel,
    ProtocolsModel,
)

router = APIRouter()


@cache(expire=120)
async def get_smartsheet(settings: Settings, sheet_id: int) -> str:
    """
    Download and cache smartsheet object as a json string.
    Parameters
    ----------
    settings : Settings
    sheet_id : int

    Returns
    -------
    str

    """

    client = Smartsheet(
        user_agent=settings.user_agent,
        max_connections=settings.max_connections,
        access_token=(settings.access_token.get_secret_value()),
    )
    sheet = await to_thread(client.Sheets.get_sheet, sheet_id)
    return sheet.to_json()


@router.get(
    "/healthcheck",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
def get_health() -> HealthCheck:
    """
    ## Endpoint to perform a healthcheck on.

    Returns:
        HealthCheck: Returns a JSON response with the health status
    """
    return HealthCheck()


@router.get(
    "/funding",
    response_model=List[FundingModel],
)
async def get_funding(
    settings: Settings = Depends(get_settings),
    project_name: Optional[str] = Query(
        default=None,
        openapi_examples={
            "default": {
                "summary": "A sample project name",
                "description": "Example project name for smartsheet",
                "value": "Discovery-Neuromodulator circuit dynamics"
                " during foraging",
            }
        },
    ),
    subproject: Optional[str] = Query(
        default=None,
        openapi_examples={
            "default": {
                "summary": "A sample subproject",
                "description": "Example subproject name",
                "value": "Subproject 2 Molecular Anatomy Cell Types",
            }
        },
    ),
):
    """
    ## Funding
    Returns funding information for a project_name and subproject.
    """

    sheet_id = settings.funding_id
    raw_sheet = await get_smartsheet(settings=settings, sheet_id=sheet_id)
    handler = SheetHandler(raw_sheet=raw_sheet)
    funding_models = handler.get_project_funding_info(
        project_name=project_name,
        subproject=subproject,
    )
    return funding_models


@router.get(
    "/project_names",
    response_model=List[str],
)
async def get_project_names(settings: Settings = Depends(get_settings)):
    """
    ## Project Names
    Returns a list of project names.
    """
    sheet_id = settings.funding_id
    raw_sheet = await get_smartsheet(settings=settings, sheet_id=sheet_id)
    handler = SheetHandler(raw_sheet=raw_sheet)
    content = handler.get_project_names()
    return content


@router.get(
    "/protocols",
    response_model=List[ProtocolsModel],
)
async def get_protocols(
    protocol_name: Optional[str] = Query(
        default=None,
        openapi_examples={
            "default": {
                "summary": "A sample protocol name",
                "description": "Example protocol name",
                "value": (
                    "Tetrahydrofuran and Dichloromethane Delipidation of a "
                    "Whole Mouse Brain"
                ),
            }
        },
    ),
    settings: Settings = Depends(get_settings),
):
    """
    ## Protocols
    Returns protocols given a name.
    """
    sheet_id = settings.protocols_id
    raw_sheet = await get_smartsheet(settings=settings, sheet_id=sheet_id)
    handler = SheetHandler(raw_sheet=raw_sheet)
    content = handler.get_protocols_info(protocol_name=protocol_name)
    return content


@router.get(
    "/perfusions",
    response_model=List[PerfusionsModel],
)
async def get_perfusions(
    subject_id: Optional[str] = Query(
        default=None,
        openapi_examples={
            "default": {
                "summary": "A sample subject id",
                "description": "Example subject id",
                "value": "689418",
            }
        },
    ),
    settings: Settings = Depends(get_settings),
):
    """
    ## Perfusions
    Returns perfusions for a given subject_id.
    """
    sheet_id = settings.perfusions_id
    raw_sheet = await get_smartsheet(settings=settings, sheet_id=sheet_id)
    handler = SheetHandler(raw_sheet=raw_sheet)
    content = handler.get_perfusions_info(subject_id=subject_id)
    return content
