from fastapi import APIRouter, HTTPException

from bin_lookup_api.api.models import BinResponse
from bin_lookup_api.services.bin_service import get_bin_data
from starlette.requests import Request

router = APIRouter()


@router.get("/lookup/{bin}", response_model=BinResponse)
async def lookup(request: Request, bin: str):

    if not bin.isdigit():
        raise HTTPException(status_code=400, detail="BIN must be a numeric value")

    if len(bin) < 6 or len(bin) > 8:
        raise HTTPException(status_code=400, detail="BIN must be between 6 and 8 digits")

    data = await get_bin_data(int(bin))
    if data is None:
        raise HTTPException(status_code=404, detail="BIN not found")

    return data
