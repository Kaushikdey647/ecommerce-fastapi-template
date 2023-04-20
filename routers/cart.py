from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schema

from database import get_db

router = APIRouter(
    prefix="/cart",
    responses={404: {"description": "Not found"}}
)

@router.get("/", response_model=list[schema.Cart])
def read_cart(user_id: int, db: Session = Depends(get_db)):
    cart = crud.get_cart_by_user_id(db, user_id=user_id)
    return cart

@router.post("/", response_model=schema.Cart)
def add_to_cart(cart: schema.CartCreate, db: Session = Depends(get_db)):
    db_cart = crud.add_product_to_cart(db, cart=cart)
    if db_cart is None:
        raise HTTPException(status_code=404, detail="Cannot Add Product to Cart")
    return db_cart