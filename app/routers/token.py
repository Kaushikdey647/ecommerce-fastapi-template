from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from datetime import timedelta
from app import schema
from fastapi.security import OAuth2PasswordRequestForm
from app.security.authentication import authenticate_user, generate_access_token
from config import ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter(
    prefix="/token",
    tags=["Token"],
    responses={404: {"description": "Not found"}}
)

@router.get("/", response_model=schema.Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    """
    Obtain an access token for authentication.

    This endpoint allows users to obtain an access token by providing their
    username and password. The access token can be used for authentication in
    protected endpoints.

    Args:
        form_data (OAuth2PasswordRequestForm): The form data containing the
        username and password.

    Returns:
        schema.Token: The access token and its type ("bearer").

    Raises:
        HTTPException: If the provided username or password is incorrect.

    Example:
        - You can send a GET request with a valid username and password to
        obtain an access token.

    """

    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = generate_access_token(user, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
