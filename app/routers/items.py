from fastapi import APIRouter, Depends
from typing import Annotated
from app.security.authentication import oauth2_scheme

router = APIRouter()

@router.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}