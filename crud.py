# Written by: Kaushik Dey
# Date: 18/04/2023
# Description: This file contains the crud utils.

from sqlalchemy.orm import Session

import models, schema

# USER

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

# PRODUCT

def get_product_list(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def get_product_by_id(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.product_id == product_id).first()

# CART

def get_cart_by_user_id(db: Session, user_id: int):
    return db.query(models.Cart).filter(models.Cart.user_id == user_id).all()

def add_product_to_cart(db: Session, cart: schema.CartCreate):
    db_cart = models.Cart(**cart.dict())
    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)
    return db_cart

# ORDER

def create_order(db: Session, order: schema.OrderCreate):
    db_order = models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders_by_user_id(db: Session, user_id: int):
    return db.query(models.Order).filter(models.Order.user_id == user_id).all()

def get_order_by_id(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.order_id == order_id).first()

def update_order_status_by_id(db: Session, order_id: int, status_id: int):
    db.query(models.Order).filter(models.Order.order_id == order_id).update({models.Order.status_id: status_id})
    db.commit()
    return db.query(models.Order).filter(models.Order.order_id == order_id).first()

# CUSTOMER SERVICE

def get_inquiries_by_id(db: Session, inquiry_id: int):
    return db.query(models.CustomerService).filter(models.CustomerService.inquiry_id == inquiry_id).first()

def get_inquiries_list(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CustomerService).offset(skip).limit(limit).all()

def get_inquiries_by_user_id(db: Session, user_id: int):
    return db.query(models.CustomerService).filter(models.CustomerService.user_id == user_id).all()

def add_inquiry(db: Session, inquiry: schema.CustomerServiceCreate):
    db_inquiry = models.CustomerService(**inquiry.dict())
    db.add(db_inquiry)
    db.commit()
    db.refresh(db_inquiry)
    return db_inquiry
