"""Starts and runs a FastAPI Server"""

import logging
import os
from asyncio import Semaphore, create_task
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from fastapi_cache.backends.redis import RedisBackend
from redis.asyncio import from_url  # noqa

from aind_smartsheet_service_server import __version__ as service_version
from aind_smartsheet_service_server.configs import settings
from aind_smartsheet_service_server.route import EXASPIM_SHEETS, router
from aind_smartsheet_service_server.sheet_cache import SheetIndexCache

# The log level can be set by adding an environment variable before launch.
log_level = os.getenv("LOG_LEVEL", "INFO")
logging.basicConfig(level=log_level)

description = """
## aind-smartsheet-service

Service to pull data from SmartSheet.

"""


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    """Init cache and add to lifespan of app"""
    # noinspection PyUnresolvedReferences
    app.state.sheet_index_cache = SheetIndexCache(
        access_token=settings.access_token_2.get_secret_value(),
        user_agent=settings.user_agent,
        semaphore=Semaphore(settings.app_concurrency_limit),
    )
    if settings.redis_url is not None:
        redis = from_url(settings.redis_url.unicode_string())
        FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    else:
        FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")
    refresh_task = None
    if settings.cache_refresh_interval > 0:
        refresh_task = create_task(
            app.state.sheet_index_cache.refresh_periodically(
                sheets=[(s_id, c_id) for s_id, _, c_id in EXASPIM_SHEETS],
                interval=settings.cache_refresh_interval,
            )
        )
    yield
    if refresh_task is not None:
        refresh_task.cancel()


# noinspection PyTypeChecker
app = FastAPI(
    title="aind-smartsheet-service",
    description=description,
    summary="Serves data from SmartSheet.",
    version=service_version,
    lifespan=lifespan,
)

# noinspection PyTypeChecker
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)
app.include_router(router)
