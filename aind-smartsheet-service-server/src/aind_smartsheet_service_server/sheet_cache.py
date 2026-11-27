"""Module to download sheets from the Smartsheet REST API and cache them"""

import json
from asyncio import Lock, Semaphore, sleep, to_thread
from collections import defaultdict
from typing import Any, Dict, List

import httpx
from fastapi import HTTPException
from fastapi_cache import FastAPICache
from smartsheet import __api_base__

from aind_smartsheet_service_server.handler import default_row_map
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


def build_index(
    sheet: SheetFields, column_id: int
) -> Dict[str, List[Dict[str, Any]]]:
    """
    Group a sheet's rows by the display value in one column.
    Parameters
    ----------
    sheet : SheetFields
    column_id : int
      Column to index on, e.g., the specimen ID column.

    Returns
    -------
    Dict[str, List[Dict[str, Any]]]
      Maps each display value to its rows, mapped with default_row_map.

    """
    index = defaultdict(list)
    for row in sheet.rows:
        for cell in row.cells:
            if cell.columnId == column_id and cell.displayValue is not None:
                index[cell.displayValue].append(default_row_map(row))
                break
    return dict(index)


class SheetIndexCache:
    """Caches sheets indexed by a column so lookups don't need the whole
    sheet. Only one download per sheet runs at a time in a process."""

    def __init__(
        self,
        access_token: str,
        user_agent: str,
        semaphore: Semaphore,
        expire: int = 600,
    ):
        """
        Class constructor
        Parameters
        ----------
        access_token : str
        user_agent : str
        semaphore : Semaphore
          Limits the number of sheets downloaded at once.
        expire : int
          Seconds until a cached index expires.
        """
        self.access_token = access_token
        self.user_agent = user_agent
        self.semaphore = semaphore
        self.expire = expire
        self._locks: Dict[str, Lock] = defaultdict(Lock)

    @staticmethod
    def _key(sheet_id: int, column_id: int) -> str:
        """Cache key for a sheet's index"""
        return f"{FastAPICache.get_prefix()}:index:{sheet_id}:{column_id}"

    async def get(
        self, sheet_id: int, column_id: int, refresh: bool = False
    ) -> Dict[str, List[Dict[str, Any]]]:
        """
        Get a sheet's index from the cache, downloading it if it is missing
        or if refresh is True.
        Parameters
        ----------
        sheet_id : int
        column_id : int
        refresh : bool
          Download the sheet even if it is cached. Default is False.

        Returns
        -------
        Dict[str, List[Dict[str, Any]]]

        """
        key = self._key(sheet_id, column_id)
        backend = FastAPICache.get_backend()
        if not refresh and (cached := await backend.get(key)) is not None:
            return json.loads(cached)
        async with self._locks[key]:
            # Another request may have filled the cache while we waited
            if not refresh and (cached := await backend.get(key)) is not None:
                return json.loads(cached)
            async with self.semaphore:
                sheet = await fetch_sheet(
                    sheet_id=sheet_id,
                    user_agent=self.user_agent,
                    access_token=self.access_token,
                )
            index = await to_thread(build_index, sheet, column_id)
            await backend.set(key, json.dumps(index), expire=self.expire)
        return index
