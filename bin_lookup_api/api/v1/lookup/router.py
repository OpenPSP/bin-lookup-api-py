from fastapi import APIRouter

from . import handlers

ROUTE_PREFIX: str = "/v1"

router = APIRouter()
router.include_router(handlers.router, prefix=ROUTE_PREFIX, tags=["Lookup"])
