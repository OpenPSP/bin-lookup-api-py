""" Api Routes
"""

from fastapi import APIRouter

from . import handlers

ROUTE_PREFIX: str = "/api/v1/healthcheck"

api_router = APIRouter()
api_router.include_router(handlers.router, prefix=ROUTE_PREFIX, tags=["HealthCheck"])
