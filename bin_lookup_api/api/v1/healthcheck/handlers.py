""" Api definition
    All validations and mappings should be in the services
"""

from fastapi import APIRouter, Depends, HTTPException, status
from starlette.requests import Request

from bin_lookup_api.settings import settings

from .models import HealthCheckResponse


router = APIRouter()


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheckResponse
    # responses={
    #     status.HTTP_500_INTERNAL_SERVER_ERROR: {
    #         "model": ApiMessage,
    #     },
    #     status.HTTP_503_SERVICE_UNAVAILABLE: {
    #         "model": ApiMessage,
    #     },
    # },
)
async def get(
    request: Request,
) -> HealthCheckResponse:

    return HealthCheckResponse(status="Healthy", version=settings.PROJECT_VERSION)
