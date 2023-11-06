from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schema

from database import get_db

router = APIRouter(
    prefix="/orders",
    responses={404: {"description": "Not found"}},
    tags=["Orders"]
)

@router.get("/", response_model=list[schema.Order])
def read_orders(user_id: int, db: Session = Depends(get_db)):
    """
    Get a list of orders by user ID.

    This endpoint retrieves a list of orders for a specific user based on their
    user ID.

    Args:
        user_id (int): The ID of the user whose orders are to be retrieved.
        db (Session): The database session.

    Returns:
        List[schema.Order]: A list of orders for the specified user.

    Raises:
        HTTPException: If there's an issue with retrieving the orders.

    Example:
        - You can send a GET request with a user ID to retrieve their orders.

    """
    orders = crud.get_orders_by_user_id(db, user_id=user_id)
    return orders

@router.get("/{order_id}", response_model=schema.Order)
def read_order(order_id: int, db: Session = Depends(get_db)):
    """
    Get order by ID.

    This endpoint retrieves an order by its unique identifier (ID).

    Args:
        order_id (int): The ID of the order to retrieve.
        db (Session): The database session.

    Returns:
        schema.Order: The order information.

    Raises:
        HTTPException: If the specified order is not found.

    Example:
        - You can send a GET request with an order ID to retrieve its details.

    """
    db_order = crud.get_order_by_id(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@router.put("/{order_id}/status", response_model=schema.Order)
def update_order_status(order_id: int, status: schema.OrderStatus, db: Session = Depends(get_db)):
    """
    Update the status of an order.

    This endpoint allows you to update the status of an existing order by providing
    its ID and the updated status.

    Args:
        order_id (int): The ID of the order to update.
        status (schema.OrderStatus): The updated status for the order.
        db (Session): The database session.

    Returns:
        schema.Order: The updated order's information.

    Raises:
        HTTPException: If the specified order is not found or there's an issue
        with the update.

    Example:
        - You can send a PUT request with an order ID and updated status to modify
        the order's status.

    """
    db_order = crud.get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return crud.update_order(db=db, order=db_order, status=status)

@router.get("/all", response_model=list[schema.Order])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Get a list of all orders with optional pagination.

    This endpoint retrieves a list of all orders with optional pagination.

    Args:
        skip (int): The number of items to skip for pagination.
        limit (int): The maximum number of items to return for pagination.
        db (Session): The database session.

    Returns:
        List[schema.Order]: A list of all orders.

    Raises:
        HTTPException: If there's an issue with retrieving the orders.

    Example:
        - You can send a GET request to retrieve a list of all orders.

    """
    orders = crud.get_order_list(db, skip=skip, limit=limit)
    return orders
