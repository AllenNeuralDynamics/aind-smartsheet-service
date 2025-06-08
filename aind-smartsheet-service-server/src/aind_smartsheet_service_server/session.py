"""Module to handle requests session"""

from aind_smartsheet_api.client import SmartsheetClient, SmartsheetSettings

from aind_smartsheet_service_server.configs import Settings

settings = Settings()


def get_session():
    """
    Yield a session object. This will automatically close the session when
    finished.
    """
    smartsheet_settings = SmartsheetSettings(
        access_token=settings.access_token,
        user_agent=settings.user_agent,
        max_connections=settings.max_connections,
        sheet_id_map={
            "funding": settings.funding_id,
            "protocols": settings.protocols_id,
            "perfusions": settings.perfusions_id,
        },
    )
    yield SmartsheetClient(smartsheet_settings=smartsheet_settings)
