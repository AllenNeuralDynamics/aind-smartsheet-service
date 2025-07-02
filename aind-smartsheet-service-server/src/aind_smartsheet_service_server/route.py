"""Module to handle endpoint responses"""

from typing import List, Optional

from fastapi import APIRouter, Depends, Query, status

from aind_smartsheet_service_server.handler import SessionHandler
from aind_smartsheet_service_server.models import (
    FundingModel,
    HealthCheck,
    PerfusionsModel,
    ProtocolsModel,
)
from aind_smartsheet_service_server.session import (
    SmartsheetClient,
    get_session,
)

router = APIRouter()


@router.get(
    "/healthcheck",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
async def get_health() -> HealthCheck:
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
def get_funding(
    project_name: Optional[str] = Query(
        default=None,
        examples=["Discovery-Neuromodulator circuit dynamics during foraging"],
    ),
    subproject: Optional[str] = Query(
        default=None,
        examples=["Subproject 2 Molecular Anatomy Cell Types"],
    ),
    session: SmartsheetClient = Depends(get_session),
):
    """
    ## Funding
    Returns funding information for a project_name and subproject.
    """
    handler = SessionHandler(session=session)
    #  TODO: Cache sheet in redis
    sheet: List[FundingModel] = handler.get_parsed_sheet(
        sheet_id=session.smartsheet_settings.sheet_id_map["funding"],
        model=FundingModel,
    )
    content = SessionHandler(session=session).get_project_funding_info(
        sheet_model=sheet, project_name=project_name, subproject=subproject
    )
    return content


@router.get(
    "/project_names",
    response_model=List[str],
)
def get_project_names(
    session: SmartsheetClient = Depends(get_session),
):
    """
    ## Project Names
    Returns a list of project names.
    """
    handler = SessionHandler(session=session)
    #  TODO: Cache sheet in redis
    sheet: List[FundingModel] = handler.get_parsed_sheet(
        sheet_id=session.smartsheet_settings.sheet_id_map["funding"],
        model=FundingModel,
    )
    content = SessionHandler(session=session).get_project_names(
        sheet_model=sheet
    )
    return content


@router.get(
    "/protocols",
    response_model=List[ProtocolsModel],
)
def get_protocols(
    protocol_name: Optional[str] = Query(
        default=None,
        examples=[
            (
                "Tetrahydrofuran and Dichloromethane Delipidation of a Whole "
                "Mouse Brain"
            )
        ],
    ),
    session: SmartsheetClient = Depends(get_session),
):
    """
    ## Protocols
    Returns protocols given a name.
    """
    handler = SessionHandler(session=session)
    #  TODO: Cache sheet in redis
    sheet: List[ProtocolsModel] = handler.get_parsed_sheet(
        sheet_id=session.smartsheet_settings.sheet_id_map["protocols"],
        model=ProtocolsModel,
    )
    content = SessionHandler(session=session).get_protocols_info(
        sheet_model=sheet, protocol_name=protocol_name
    )
    return content


@router.get(
    "/perfusions",
    response_model=List[PerfusionsModel],
)
def get_perfusions(
    subject_id: Optional[str] = Query(
        default=None,
        examples=["689418"],
    ),
    session: SmartsheetClient = Depends(get_session),
):
    """
    ## Perfusions
    Returns perfusions for a given subject_id.
    """
    handler = SessionHandler(session=session)
    # TODO: Cache sheet in redis
    sheet: List[PerfusionsModel] = handler.get_parsed_sheet(
        sheet_id=session.smartsheet_settings.sheet_id_map["perfusions"],
        model=PerfusionsModel,
    )
    content = SessionHandler(session=session).get_perfusions_info(
        sheet_model=sheet, subject_id=subject_id
    )
    return content
