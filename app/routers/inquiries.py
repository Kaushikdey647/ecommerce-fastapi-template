from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schema

from database import get_db

router = APIRouter(
    prefix="/inquiries",
    responses={404: {"description": "Not found"}}
)

@router.get("/", response_model=list[schema.CustomerService])
def read_inquiries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Get a list of customer inquiries.

    This endpoint retrieves a list of customer inquiries with optional pagination.

    Args:
        skip (int): The number of items to skip for pagination.
        limit (int): The maximum number of items to return for pagination.
        db (Session): The database session.

    Returns:
        List[schema.CustomerService]: A list of customer inquiries.

    Raises:
        HTTPException: If there's an issue with retrieving the inquiries.

    Example:
        - You can send a GET request to retrieve a list of customer inquiries.

    """
    inquiries = crud.get_inquiries_list(db, skip=skip, limit=limit)
    return inquiries

@router.post("/", response_model=schema.CustomerService)
def create_inquiry(inquiry: schema.CustomerServiceCreate, db: Session = Depends(get_db)):
    """
    Create a new customer inquiry.

    This endpoint allows you to create a new customer inquiry with the provided information.

    Args:
        inquiry (schema.CustomerServiceCreate): The data to create a new inquiry.
        db (Session): The database session.

    Returns:
        schema.CustomerService: The created customer inquiry.

    Raises:
        HTTPException: If there's an issue with inquiry creation.

    Example:
        - You can send a POST request with inquiry data to create a new customer inquiry.

    """
    db_inquiry = crud.add_inquiry(db, inquiry=inquiry)
    return db_inquiry

@router.get("/{inquiry_id}", response_model=schema.CustomerService)
def read_inquiry(inquiry_id: int, db: Session = Depends(get_db)):
    """
    Get a customer inquiry by ID.

    This endpoint retrieves a customer inquiry by its unique identifier (ID).

    Args:
        inquiry_id (int): The ID of the inquiry to retrieve.
        db (Session): The database session.

    Returns:
        schema.CustomerService: The customer inquiry information.

    Raises:
        HTTPException: If the specified inquiry is not found.

    Example:
        - You can send a GET request with an inquiry ID to retrieve its details.

    """
    db_inquiry = crud.get_inquiry_by_id(db, inquiry_id=inquiry_id)
    if db_inquiry is None:
        raise HTTPException(status_code=404, detail="Inquiry not found")
    return db_inquiry
