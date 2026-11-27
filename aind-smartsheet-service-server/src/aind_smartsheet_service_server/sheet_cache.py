"""Module to download sheets from the Smartsheet REST API"""

from asyncio import sleep, to_thread

import httpx
from fastapi import HTTPException
from smartsheet import __api_base__

from aind_smartsheet_service_server.models import SheetFields

RETRY_STATUS_CODES = {429, 500, 502, 503, 504}
MAX_ATTEMPTS = 3


async def fetch_sheet(
    sheet_id: int, user_agent: str, access_token: str
) -> SheetFields:
    """
    Download a sheet directly from the Smartsheet REST API. This skips the
    Smartsheet SDK's object model, which is much slower for large sheets.
    Rate limit and server errors are retried with exponential backoff.

    Parameters
    ----------
    sheet_id : int
    user_agent : str
    access_token : str

    Returns
    -------
    SheetFields or raises HTTPException

    """
    headers = {"Authorization": f"Bearer {access_token}"}
    if user_agent:
        headers["User-Agent"] = user_agent
    async with httpx.AsyncClient(timeout=120) as client:
        for attempt in range(MAX_ATTEMPTS):
            response = await client.get(
                f"{__api_base__}/sheets/{sheet_id}", headers=headers
            )
            if (
                response.status_code not in RETRY_STATUS_CODES
                or attempt == MAX_ATTEMPTS - 1
            ):
                break
            await sleep(2**attempt)
    if response.is_error:
        try:
            message = response.json().get("message")
        except ValueError:
            message = None
        raise HTTPException(
            status_code=response.status_code,
            detail=message or "Smartsheet error",
        )
    return await to_thread(SheetFields.model_validate_json, response.content)
