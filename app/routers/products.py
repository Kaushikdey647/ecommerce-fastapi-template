from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schema

from database import get_db

router = APIRouter(
    prefix="/products",
    responses={404: {"description": "Not found"}},
    tags=["Products"]
)

@router.get("/", response_model=list[schema.Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Get a list of products.

    This endpoint retrieves a list of products with optional pagination.

    Args:
        skip (int): The number of items to skip for pagination.
        limit (int): The maximum number of items to return for pagination.
        db (Session): The database session.

    Returns:
        List[schema.Product]: A list of products.

    Raises:
        HTTPException: If there's an issue with retrieving the product list.

    Example:
        - You can send a GET request to retrieve a list of products.

    """
    products = crud.get_product_list(db, skip=skip, limit=limit)
    return products

@router.get("/{product_id}", response_model=schema.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    """
    Get product by ID.

    This endpoint retrieves a product by its unique identifier (ID).

    Args:
        product_id (int): The ID of the product to retrieve.
        db (Session): The database session.

    Returns:
        schema.Product: The product information.

    Raises:
        HTTPException: If the specified product is not found.

    Example:
        - You can send a GET request with a product ID to retrieve its details.

    """
    db_product = crud.get_product_by_id(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.post("/", response_model=schema.Product)
def create_product(product: schema.ProductCreate, db: Session = Depends(get_db)):
    """
    Create a new product.

    This endpoint allows you to create a new product with the provided information.

    Args:
        product (schema.ProductCreate): The data to create a new product.
        db (Session): The database session.

    Returns:
        schema.Product: The created product's information.

    Raises:
        HTTPException: If there's an issue with product creation.

    Example:
        - You can send a POST request with product data to create a new product.

    """
    db_product = crud.add_product(db, product=product)
    return db_product

@router.put("/{product_id}", response_model=schema.Product)
def update_product(product_id: int, product: schema.ProductUpdate, db: Session = Depends(get_db)):
    """
    Update an existing product.

    This endpoint allows you to update an existing product by providing its ID and
    the updated data.

    Args:
        product_id (int): The ID of the product to update.
        product (schema.ProductUpdate): The updated product data.
        db (Session): The database session.

    Returns:
        schema.Product: The updated product's information.

    Raises:
        HTTPException: If the specified product is not found or there's an issue
        with the update.

    Example:
        - You can send a PUT request with a product ID and updated data to modify
        an existing product.

    """
    db_product = crud.get_product_by_id(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud.update_product(db=db, product=db_product, product_update=product)

@router.delete("/{product_id}", response_model=schema.Product)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """
    Delete a product by ID.

    This endpoint allows you to delete a product by providing its unique identifier (ID).

    Args:
        product_id (int): The ID of the product to delete.
        db (Session): The database session.

    Returns:
        schema.Product: The deleted product's information.

    Raises:
        HTTPException: If the specified product is not found or there's an issue
        with deletion.

    Example:
        - You can send a DELETE request with a product ID to delete the product.

    """
    db_product = crud.get_product_by_id(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud.delete_product(db=db, product_id=product_id)
