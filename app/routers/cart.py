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
    """
    Retrieve the user's shopping cart.

    This endpoint retrieves the shopping cart for a specific user based on their
    user ID.

    Args:
        user_id (int): The ID of the user whose cart is to be retrieved.
        db (Session): The database session.

    Returns:
        List[schema.Cart]: A list of items in the user's shopping cart.

    Raises:
        HTTPException: If there's an issue with retrieving the cart.

    Example:
        - You can send a GET request with a user ID to retrieve the items in the user's
        shopping cart.

    """
    cart = crud.get_cart_by_user_id(db, user_id=user_id)
    return cart

@router.post("/", response_model=schema.Cart)
def add_to_cart(cart: schema.CartCreate, db: Session = Depends(get_db)):
    """
    Add a product to the user's shopping cart.

    This endpoint allows you to add a product to the user's shopping cart with the
    provided information.

    Args:
        cart (schema.CartCreate): The data to add a product to the user's cart.
        db (Session): The database session.

    Returns:
        schema.Cart: The updated shopping cart, including the newly added product.

    Raises:
        HTTPException: If there's an issue with adding the product to the cart.

    Example:
        - You can send a POST request with product data to add it to the user's shopping cart.

    """
    db_cart = crud.add_product_to_cart(db, cart=cart)
    if db_cart is None:
        raise HTTPException(status_code=404, detail="Cannot Add Product to Cart")
    return db_cart
