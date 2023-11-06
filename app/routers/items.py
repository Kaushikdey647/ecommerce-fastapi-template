from fastapi import APIRouter, Depends
from typing import Annotated
from app.security.authentication import oauth2_scheme

router = APIRouter(
    prefix="/items",
    responses={404: {"description": "Not found"}},
    tags=["Items"]
)

@router.get("/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    """
    Retrieve items with authentication.

    This endpoint retrieves a list of items while requiring authentication using an
    OAuth2 token. Users must provide a valid token in the request headers to access
    this endpoint.

    Args:
        token (str): An OAuth2 token obtained from the authentication process.

    Returns:
        dict: A dictionary containing the provided token.

    Example:
        - You can send a GET request with a valid OAuth2 token in the request headers
        to retrieve a list of items while authenticating the user.

    """
    return {"token": token}
