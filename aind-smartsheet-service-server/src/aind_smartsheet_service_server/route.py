"""Module to handle endpoint responses"""

from asyncio import gather, to_thread
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query, Request, status
from fastapi.openapi.models import Example
from fastapi_cache.decorator import cache
from smartsheet import Smartsheet
from smartsheet.models.error import Error as SmartsheetError

from aind_smartsheet_service_server.configs import settings
from aind_smartsheet_service_server.exaspim_models import (
    ExaSPIMInfo,
    ImagingQueue,
    MouseTracker,
    QcSheet,
    SampleTracking,
)
from aind_smartsheet_service_server.handler import (
    SheetHandler,
    default_row_filter,
)
from aind_smartsheet_service_server.models import (
    FundingModel,
    HealthCheck,
    PerfusionsModel,
    ProtocolsModel,
    SheetFields,
)

router = APIRouter()


@cache(expire=600)
async def get_smartsheet(
    sheet_id: int, user_agent: str, max_connections: int, access_token: str
) -> dict:
    """
    Download and cache smartsheet object as a json string.
    Parameters
    ----------
    sheet_id : int
    user_agent : str
    max_connections : int
    access_token : str

    Returns
    -------
    dict or raises Exception
    """

    client = Smartsheet(
        user_agent=user_agent,
        max_connections=max_connections,
        access_token=access_token,
    )
    sheet = await to_thread(client.Sheets.get_sheet, sheet_id)

    if isinstance(sheet, SmartsheetError):
        sheet_status = sheet.result.status_code
        message = sheet.result.message or "Smartsheet error"
        raise HTTPException(status_code=sheet_status, detail=message)
    sheet_fields = SheetFields.model_validate_json(json_data=sheet.to_json())
    return sheet_fields.model_dump(mode="json", exclude_none=True)


@router.get(
    "/healthcheck",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
    operation_id="get_health",
)
async def get_health() -> HealthCheck:
    """
    ## Endpoint to perform a healthcheck on.

    Returns:
        HealthCheck: Returns a JSON response with the health status
    """
    return HealthCheck()


@router.get(
    "/funding", response_model=List[FundingModel], operation_id="get_funding"
)
async def get_funding(
    project_name: Optional[str] = Query(
        default=None,
        openapi_examples={
            "default": Example(
                summary="A sample project name",
                description="Example project name for smartsheet",
                value=("Discovery Neuromodulation"),
            )
        },
    ),
    subproject: Optional[str] = Query(
        default=None,
        openapi_examples={
            "default": Example(
                summary="A sample subproject",
                description="Example subproject name",
                value="Subproject 2 Molecular Anatomy Cell Types",
            )
        },
    ),
):
    """
    ## Funding
    Returns funding information for a project_name and subproject.
    """

    sheet_id = settings.funding_id
    raw_sheet = await get_smartsheet(
        sheet_id=sheet_id,
        user_agent=settings.user_agent,
        max_connections=settings.max_connections,
        access_token=settings.access_token.get_secret_value(),
    )
    handler = SheetHandler(sheet_fields=SheetFields.model_validate(raw_sheet))
    funding_models: List[FundingModel] = handler.get_parsed_sheet_model(
        model=FundingModel
    )
    filtered_rows = [
        r
        for r in funding_models
        if (
            r.project_name == project_name
            and (subproject is None or r.subproject == subproject)
        )
        or (project_name is None and subproject is None)
    ]
    return filtered_rows


@router.get(
    "/project_names",
    response_model=List[str],
    operation_id="get_project_names",
)
async def get_project_names():
    """
    ## Project Names
    Returns a list of project names.
    """
    sheet_id = settings.funding_id
    raw_sheet = await get_smartsheet(
        sheet_id=sheet_id,
        user_agent=settings.user_agent,
        max_connections=settings.max_connections,
        access_token=settings.access_token.get_secret_value(),
    )
    handler = SheetHandler(sheet_fields=SheetFields.model_validate(raw_sheet))
    funding_models: List[FundingModel] = handler.get_parsed_sheet_model(
        model=FundingModel
    )
    project_names = set()
    for funding_model in funding_models:
        project_name = funding_model.project_name
        subproject_name = funding_model.subproject
        if project_name is not None and subproject_name is None:
            project_names.add(project_name)
        elif project_name is not None and subproject_name is not None:
            project_names.add(f"{project_name} - {subproject_name}")
    sorted_names = sorted(list(set(project_names)))
    return sorted_names


@router.get(
    "/protocols",
    response_model=List[ProtocolsModel],
    operation_id="get_protocols",
)
async def get_protocols(
    protocol_name: Optional[str] = Query(
        default=None,
        openapi_examples={
            "default": Example(
                summary="A sample protocol name",
                description="Example protocol name",
                value=(
                    "Tetrahydrofuran and Dichloromethane Delipidation of a "
                    "Whole Mouse Brain"
                ),
            )
        },
    )
):
    """
    ## Protocols
    Returns protocols given a name.
    """
    sheet_id = settings.protocols_id
    raw_sheet = await get_smartsheet(
        sheet_id=sheet_id,
        user_agent=settings.user_agent,
        max_connections=settings.max_connections,
        access_token=settings.access_token.get_secret_value(),
    )
    handler = SheetHandler(
        sheet_fields=SheetFields.model_validate(raw_sheet),
        row_filter=lambda row: default_row_filter(
            row=row,
            column_id=(
                None
                if protocol_name is None
                else int(
                    ProtocolsModel.model_fields[
                        "protocol_name"
                    ].validation_alias
                )
            ),
            column_display_value=protocol_name,
        ),
    )
    parsed_models = handler.get_parsed_sheet_model(model=ProtocolsModel)
    return parsed_models


@router.get(
    "/perfusions",
    response_model=List[PerfusionsModel],
    operation_id="get_perfusions",
)
async def get_perfusions(
    subject_id: Optional[str] = Query(
        default=None,
        openapi_examples={
            "default": Example(
                summary="A sample subject id",
                description="Example subject id",
                value="689418",
            )
        },
    )
):
    """
    ## Perfusions
    Returns perfusions for a given subject_id.
    """
    sheet_id = settings.perfusions_id
    raw_sheet = await get_smartsheet(
        sheet_id=sheet_id,
        user_agent=settings.user_agent,
        max_connections=settings.max_connections,
        access_token=settings.access_token.get_secret_value(),
    )
    handler = SheetHandler(
        sheet_fields=SheetFields.model_validate(raw_sheet),
        row_filter=lambda row: default_row_filter(
            row=row,
            column_id=(
                None
                if subject_id is None
                else int(
                    PerfusionsModel.model_fields["subject_id"].validation_alias
                )
            ),
            column_display_value=subject_id,
        ),
    )
    parsed_models = handler.get_parsed_sheet_model(model=PerfusionsModel)
    return parsed_models


@router.get(
    "/get_exaspim_info",
    response_model=ExaSPIMInfo,
    response_model_exclude_none=True,
    operation_id="get_exaspim_info",
)
async def get_exaspim_info(
    request: Request,
    specimen_id: str = Query(
        ...,
        openapi_examples={
            "default": Example(
                summary="An example specimen ID",
                description="Example specimen ID",
                value="822178",
            )
        },
    ),
):
    """
    ## exaSPIM Information endpoint
    Returns exaSPIM info for a given specimen_id.
    """
    # Limit number of requests
    semaphore = request.app.state.semaphore
    async with semaphore:
        # Download sheets in parallel
        tasks = [
            get_smartsheet(
                sheet_id=settings.mouse_tracker_id,
                user_agent=settings.user_agent,
                max_connections=settings.max_connections,
                access_token=settings.access_token_2.get_secret_value(),
            ),
            get_smartsheet(
                sheet_id=settings.sample_tracking_id,
                user_agent=settings.user_agent,
                max_connections=settings.max_connections,
                access_token=settings.access_token_2.get_secret_value(),
            ),
            get_smartsheet(
                sheet_id=settings.imaging_queue_id,
                user_agent=settings.user_agent,
                max_connections=settings.max_connections,
                access_token=settings.access_token_2.get_secret_value(),
            ),
            get_smartsheet(
                sheet_id=settings.exaspim_qc_sheet_id,
                user_agent=settings.user_agent,
                max_connections=settings.max_connections,
                access_token=settings.access_token_2.get_secret_value(),
            ),
        ]
        (
            mouse_tracker_sheet,
            sample_tracker_sheet,
            imaging_queue_sheet,
            qc_sheet,
        ) = await gather(*tasks)
        mouse_tracker_handler = SheetHandler(
            sheet_fields=SheetFields.model_validate(mouse_tracker_sheet),
            row_filter=lambda row: default_row_filter(
                row=row,
                column_id=(
                    None
                    if specimen_id is None
                    else int(
                        MouseTracker.model_fields["mouse_id"].validation_alias
                    )
                ),
                column_display_value=specimen_id,
            ),
        )
        sample_tracker_handler = SheetHandler(
            sheet_fields=SheetFields.model_validate(sample_tracker_sheet),
            row_filter=lambda row: default_row_filter(
                row=row,
                column_id=(
                    None
                    if specimen_id is None
                    else int(
                        SampleTracking.model_fields["sample"].validation_alias
                    )
                ),
                column_display_value=specimen_id,
            ),
        )
        imaging_queue_handler = SheetHandler(
            sheet_fields=SheetFields.model_validate(imaging_queue_sheet),
            row_filter=lambda row: default_row_filter(
                row=row,
                column_id=(
                    None
                    if specimen_id is None
                    else int(
                        ImagingQueue.model_fields["sample"].validation_alias
                    )
                ),
                column_display_value=specimen_id,
            ),
        )
        qc_handler = SheetHandler(
            sheet_fields=SheetFields.model_validate(qc_sheet),
            row_filter=lambda row: default_row_filter(
                row=row,
                column_id=(
                    None
                    if specimen_id is None
                    else int(QcSheet.model_fields["sample"].validation_alias)
                ),
                column_display_value=specimen_id,
            ),
        )
        mouse_tracker_info = mouse_tracker_handler.get_parsed_sheet_model(
            model=MouseTracker
        )
        sample_tracking_info = sample_tracker_handler.get_parsed_sheet_model(
            model=SampleTracking
        )
        imaging_queue_info = imaging_queue_handler.get_parsed_sheet_model(
            model=ImagingQueue
        )
        qc_sheet_info = qc_handler.get_parsed_sheet_model(model=QcSheet)
        bundled_info = ExaSPIMInfo(
            mouse_tracker_info=mouse_tracker_info,
            sample_tracking_info=sample_tracking_info,
            imaging_queue_info=imaging_queue_info,
            qc_sheet_info=qc_sheet_info,
        )
    return bundled_info
