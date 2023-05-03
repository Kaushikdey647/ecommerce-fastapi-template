# Written by: Kaushik Dey
# Date: 18/04/2023
# Description: This file contains the models for the database


from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Order(Base):
    __tablename__ = "order"
    order_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True)
    date = Column(String)
    total_cost = Column(Integer)
    payment_id = Column(Integer, unique=True)
    status_id = Column(Integer, unique=True)

class OrderStatus(Base):
    __tablename__ = "order_status"
    status_id = Column(Integer, primary_key=True, index=True)
    status = Column(String)

class Payment(Base):
    __tablename__ = "payment"
    payment_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True)
    card_number = Column(String)
    card_holder = Column(String)
    expiration_date = Column(String)
    cvv = Column(Integer)

class User(Base):
    __tablename__ = "user_data"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)

class Cart(Base):
    __tablename__ = "cart"
    cart_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    product_id = Column(Integer)
    quantity = Column(Integer)

class Product(Base):
    __tablename__ = "product"
    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)
    description = Column(String)
    image_url = Column(String)

class Category(Base):
    __tablename__ = "category"
    category_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

class CustomerService(Base):
    __tablename__ = "customer_service"
    inquiry_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True)
    date = Column(String)
    message = Column(String)