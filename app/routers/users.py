from fastapi import APIRouter, Depends
from app import schema
from app.security.authentication import get_current_user
from app import crud
from app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}}
)

@router.get("/me/", response_model=schema.User)
async def read_users_me(current_user: schema.User = Depends(get_current_user)):
    """
    Get the current user's profile.

    This endpoint returns the profile of the authenticated user.

    Args:
        current_user (schema.User): The authenticated user obtained from the token.

    Returns:
        schema.User: The user's profile information.

    Raises:
        HTTPException: If the user is not authenticated.

    Example:
        - If authenticated, it returns the user's profile.

    """
    return current_user

@router.post("/", response_model=schema.User)
async def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.

    This endpoint allows you to create a new user with the provided information.

    Args:
        user (schema.UserCreate): The user data to create a new user.
        db (Session): The database session.

    Returns:
        schema.User: The created user's profile information.

    Raises:
        HTTPException: If there's an issue with user creation.

    Example:
        - You can send a POST request with user data to create a new user.

    """
    db_user = crud.create_user(db=db, user=user)
    return db_user
