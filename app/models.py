# Written by: Kaushik Dey
# Date: 18/04/2023
# Description: This file contains the models for the database.

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Order(Base):
    """
    Model for orders in the database.

    Represents an order placed by a user, including details such as the user ID, date, total cost, payment ID, and status ID.
    """
    __tablename__ = "order"
    order_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True)
    date = Column(String)
    total_cost = Column(Integer)
    payment_id = Column(Integer, unique=True)
    status_id = Column(Integer, unique=True)

class OrderStatus(Base):
    """
    Model for order statuses in the database.

    Represents possible order statuses with a unique status ID and a descriptive status string.
    """
    __tablename__ = "order_status"
    status_id = Column(Integer, primary_key=True, index=True)
    status = Column(String)

class Payment(Base):
    """
    Model for payment information in the database.

    Represents payment details, including the user ID, card number, card holder name, expiration date, and CVV.
    """
    __tablename__ = "payment"
    payment_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True)
    card_number = Column(String)
    card_holder = Column(String)
    expiration_date = Column(String)
    cvv = Column(Integer)

class User(Base):
    """
    Model for user data in the database.

    Represents user information, including a unique user ID, username, email, and password.
    """
    __tablename__ = "user_data"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)

class Cart(Base):
    """
    Model for shopping carts in the database.

    Represents the items in a user's shopping cart, including the cart ID, user ID, product ID, and quantity.
    """
    __tablename__ = "cart"
    cart_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    product_id = Column(Integer)
    quantity = Column(Integer)

class Product(Base):
    """
    Model for products in the database.

    Represents products available in the system, including the product ID, name, price, description, and image URL.
    """
    __tablename__ = "product"
    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)
    description = Column(String)
    image_url = Column(String)

class Category(Base):
    """
    Model for product categories in the database.

    Represents product categories, including the category ID and name.
    """
    __tablename__ = "category"
    category_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

class CustomerService(Base):
    """
    Model for customer service inquiries in the database.

    Represents customer service inquiries, including the inquiry ID, user ID, date, and message.
    """
    __tablename__ = "customer_service"
    inquiry_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True)
    date = Column(String)
    message = Column(String)
