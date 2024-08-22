"""Module to include the API routers for the application
"""

from fastapi import FastAPI

# Healthcheck (do not touch)
from bin_lookup_api.api.v1.healthcheck.router import (
    api_router as healthcheck_v1_router,
)
from bin_lookup_api.api.v1.lookup.router import router as lookup_v1_router
from bin_lookup_api.logging import logger


def include_routers(app: FastAPI):
    """Include routers for every application

    Args:
        app (_type_): _description_
    """
    logger.debug("Including routers")

    # Healthcheck route (do not touch)
    app.include_router(healthcheck_v1_router)

    app.include_router(lookup_v1_router)

