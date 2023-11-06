# Written by: Kaushik Dey
# Date: 18/04/2023
# Description: This file contains the CRUD utilities.

from sqlalchemy.orm import Session

import models, schema

# USER

def get_user_by_email(db: Session, email: str):
    """
    Retrieve a user by email from the database.

    Args:
        db (Session): The database session.
        email (str): The email address of the user to retrieve.

    Returns:
        models.User: The user with the specified email.
    """
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_id(db: Session, user_id: int):
    """
    Retrieve a user by their user ID from the database.

    Args:
        db (Session): The database session.
        user_id (int): The user's unique identifier.

    Returns:
        models.User: The user with the specified user ID.
    """
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def get_user_by_username(db: Session, username: str):
    """
    Retrieve a user by their username from the database.

    Args:
        db (Session): The database session.
        username (str): The username of the user to retrieve.

    Returns:
        models.User: The user with the specified username.
    """
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schema.UserCreate):
    """
    Create a new user and add them to the database.

    Args:
        db (Session): The database session.
        user (schema.UserCreate): User data for creation.

    Returns:
        models.User: The created user.
    """
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    """
    Delete a user from the database.

    Args:
        db (Session): The database session.
        user_id (int): The user's unique identifier.
    """
    db.query(models.User).filter(models.User.user_id == user_id).delete()
    db.commit()

# PRODUCT

def get_product_list(db: Session, skip: int = 0, limit: int = 100):
    """
    Get a list of products with optional pagination.

    Args:
        db (Session): The database session.
        skip (int): The number of items to skip for pagination.
        limit (int): The maximum number of items to return for pagination.

    Returns:
        List[models.Product]: A list of products.
    """
    return db.query(models.Product).offset(skip).limit(limit).all()

def get_product_by_id(db: Session, product_id: int):
    """
    Retrieve a product by its unique identifier (ID).

    Args:
        db (Session): The database session.
        product_id (int): The product's unique identifier.

    Returns:
        models.Product: The product with the specified ID.
    """
    return db.query(models.Product).filter(models.Product.product_id == product_id).first()

def add_product(db: Session, product: schema.ProductCreate):
    """
    Add a new product to the database.

    Args:
        db (Session): The database session.
        product (schema.ProductCreate): Product data for creation.

    Returns:
        models.Product: The created product.
    """
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    """
    Delete a product from the database.

    Args:
        db (Session): The database session.
        product_id (int): The product's unique identifier.
    """
    db.query(models.Product).filter(models.Product.product_id == product_id).delete()
    db.commit()

# CART

def get_cart_by_user_id(db: Session, user_id: int):
    """
    Retrieve a user's shopping cart.

    Args:
        db (Session): The database session.
        user_id (int): The user's unique identifier.

    Returns:
        List[models.Cart]: A list of items in the user's shopping cart.
    """
    return db.query(models.Cart).filter(models.Cart.user_id == user_id).all()

def add_product_to_cart(db: Session, cart: schema.CartCreate):
    """
    Add a product to a user's shopping cart in the database.

    Args:
        db (Session): The database session.
        cart (schema.CartCreate): Cart item data for addition.

    Returns:
        models.Cart: The updated shopping cart, including the newly added product.
    """
    db_cart = models.Cart(**cart.dict())
    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)
    return db_cart

# ORDER

def create_order(db: Session, order: schema.OrderCreate):
    """
    Create a new order and add it to the database.

    Args:
        db (Session): The database session.
        order (schema.OrderCreate): Order data for creation.

    Returns:
        models.Order: The created order.
    """
    db_order = models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders_list(db: Session, skip: int = 0, limit: int = 100):
    """
    Get a list of orders with optional pagination.

    Args:
        db (Session): The database session.
        skip (int): The number of items to skip for pagination.
        limit (int): The maximum number of items to return for pagination.

    Returns:
        List[models.Order]: A list of orders.
    """
    return db.query(models.Order).offset(skip).limit(limit).all()

def get_orders_by_user_id(db: Session, user_id: int):
    """
    Retrieve a user's orders.

    Args:
        db (Session): The database session.
        user_id (int): The user's unique identifier.

    Returns:
        List[models.Order]: A list of orders belonging to the user.
    """
    return db.query(models.Order).filter(models.Order.user_id == user_id).all()

def get_order_by_id(db: Session, order_id: int):
    """
    Retrieve an order by its unique identifier (ID).

    Args:
        db (Session): The database session.
        order_id (int): The order's unique identifier.

    Returns:
        models.Order: The order with the specified ID.
    """
    return db.query(models.Order).filter(models.Order.order_id == order_id).first()

def update_order_status_by_id(db: Session, order_id: int, status_id: int):
    """
    Update the status of an order by its unique identifier (ID).

    Args:
        db (Session): The database session.
        order_id (int): The order's unique identifier.
        status_id (int): The new status to set for the order.

    Returns:
        models.Order: The updated order.
    """
    db.query(models.Order).filter(models.Order.order_id == order_id).update({models.Order.status_id: status_id})
    db.commit()
    return db.query(models.Order).filter(models.Order.order_id == order_id).first()

# CUSTOMER SERVICE

def get_inquiries_by_id(db: Session, inquiry_id: int):
    """
    Retrieve a customer service inquiry by its unique identifier (ID).

    Args:
        db (Session): The database session.
        inquiry_id (int): The inquiry's unique identifier.

    Returns:
        models.CustomerService: The inquiry with the specified ID.
    """
    return db.query(models.CustomerService).filter(models.CustomerService.inquiry_id == inquiry_id).first()

def get_inquiries_list(db: Session, skip: int = 0, limit: int = 100):
    """
    Get a list of customer service inquiries with optional pagination.

    Args:
        db (Session): The database session.
        skip (int): The number of items to skip for pagination.
        limit (int): The maximum number of items to return for pagination.

    Returns:
        List[models.CustomerService]: A list of customer service inquiries.
    """
    return db.query(models.CustomerService).offset(skip).limit(limit).all()

def get_inquiries_by_user_id(db: Session, user_id: int):
    """
    Retrieve customer service inquiries for a specific user.

    Args:
        db (Session): The database session.
        user_id (int): The user's unique identifier.

    Returns:
        List[models.CustomerService]: A list of inquiries belonging to the user.
    """
    return db.query(models.CustomerService).filter(models.CustomerService.user_id == user_id).all()

def add_inquiry(db: Session, inquiry: schema.CustomerServiceCreate):
    """
    Add a new customer service inquiry to the database.

    Args:
        db (Session): The database session.
        inquiry (schema.CustomerServiceCreate): Inquiry data for creation.

    Returns:
        models.CustomerService: The created inquiry.
    """
    db_inquiry = models.CustomerService(**inquiry.dict())
    db.add(db_inquiry)
    db.commit()
    db.refresh(db_inquiry)
    return db_inquiry
