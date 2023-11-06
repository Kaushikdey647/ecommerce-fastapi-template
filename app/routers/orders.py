from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schema

from database import get_db

router = APIRouter(
    prefix="/orders",
    responses={404: {"description": "Not found"}}
)

@router.get("/", response_model=list[schema.Order])
def read_orders(user_id: int, db: Session = Depends(get_db)):
    orders = crud.get_orders_by_user_id(db, user_id=user_id)
    return orders

@router.get("/{order_id}", response_model=schema.Order)
def read_order(order_id: int, db: Session = Depends(get_db)):
    db_order = crud.get_order_by_id(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@router.put("/{order_id}/status", response_model=schema.Order)
def update_order_status(order_id: int, status: schema.OrderStatus, db: Session = Depends(get_db)):
    db_order = crud.get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return crud.update_order(db=db, order=db_order, status=status)

@router.get("/all", response_model=list[schema.Order])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    orders = crud.get_order_list(db, skip=skip, limit=limit)
    return orders