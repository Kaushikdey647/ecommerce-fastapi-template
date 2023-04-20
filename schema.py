# Written by: Kaushik Dey
# Date: 18/04/2023
# Description: This file contains the pydantic models.

from typing import List, Optional
from pydantic import BaseModel

class OrderBase(BaseModel):
    user_id: int
    date: str
    total_cost: int
    payment_id: int
    status_id: int

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    order_id: int

    class Config:
        orm_mode = True

class OrderStatusBase(BaseModel):
    status: str

class OrderStatusCreate(OrderStatusBase):
    pass

class OrderStatus(OrderStatusBase):
    status_id: int

    class Config:
        orm_mode = True

class PaymentBase(BaseModel):
    user_id: int
    card_number: str
    card_holder: str
    expiration_date: str
    cvv: int

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    payment_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    user_id: int

    class Config:
        orm_mode = True

class CartBase(BaseModel):
    user_id: int
    product_id: int
    quantity: int

class CartCreate(CartBase):
    pass

class Cart(CartBase):
    cart_id: int

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    price: int
    description: Optional[str] = None
    image_url: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    product_id: int

    class Config:
        orm_mode = True

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    category_id: int

    class Config:
        orm_mode = True

class CustomerServiceBase(BaseModel):
    user_id: int
    date: str
    message: str

class CustomerServiceCreate(CustomerServiceBase):
    pass

class CustomerService(CustomerServiceBase):
    inquiry_id: int

    class Config:
        orm_mode = True