# Written by: Kaushik Dey
# Date: 18/04/2023
# Description: This file contains the Pydantic models.

from typing import List, Optional
from pydantic import BaseModel

class OrderBase(BaseModel):
    """
    Base model for orders.

    Common fields for creating and updating orders.
    """
    user_id: int
    date: str
    total_cost: int
    payment_id: int
    status_id: int

class OrderCreate(OrderBase):
    """
    Model for creating a new order.

    Inherited from OrderBase, includes fields required for order creation.
    """
    pass

class Order(OrderBase):
    """
    Model for retrieving order details.

    Inherited from OrderBase, includes fields for displaying order information.
    """
    order_id: int

    class Config:
        orm_mode = True

class OrderStatusBase(BaseModel):
    """
    Base model for order statuses.

    Common fields for creating and updating order statuses.
    """
    status: str

class OrderStatusCreate(OrderStatusBase):
    """
    Model for creating a new order status.

    Inherited from OrderStatusBase, includes fields required for order status creation.
    """
    pass

class OrderStatus(OrderStatusBase):
    """
    Model for retrieving order status details.

    Inherited from OrderStatusBase, includes fields for displaying order status information.
    """
    status_id: int

    class Config:
        orm_mode = True

class PaymentBase(BaseModel):
    """
    Base model for payment information.

    Common fields for creating and updating payment information.
    """
    user_id: int
    card_number: str
    card_holder: str
    expiration_date: str
    cvv: int

class PaymentCreate(PaymentBase):
    """
    Model for creating a new payment record.

    Inherited from PaymentBase, includes fields required for payment record creation.
    """
    pass

class Payment(PaymentBase):
    """
    Model for retrieving payment details.

    Inherited from PaymentBase, includes fields for displaying payment information.
    """
    payment_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    """
    Base model for user data.

    Common fields for creating and updating user data.
    """
    username: str
    email: str

class UserCreate(UserBase):
    """
    Model for creating a new user.

    Inherited from UserBase, includes fields required for user creation.
    """
    password: str

class User(UserBase):
    """
    Model for retrieving user details.

    Inherited from UserBase, includes fields for displaying user information.
    """
    user_id: int

    class Config:
        orm_mode = True

class CartBase(BaseModel):
    """
    Base model for shopping cart items.

    Common fields for creating and updating shopping cart items.
    """
    user_id: int
    product_id: int
    quantity: int

class CartCreate(CartBase):
    """
    Model for adding a new item to the shopping cart.

    Inherited from CartBase, includes fields required for adding items to the cart.
    """
    pass

class Cart(CartBase):
    """
    Model for retrieving shopping cart details.

    Inherited from CartBase, includes fields for displaying shopping cart information.
    """
    cart_id: int

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    """
    Base model for product information.

    Common fields for creating and updating product information.
    """
    name: str
    price: int
    description: Optional[str] = None
    image_url: Optional[str] = None

class ProductCreate(ProductBase):
    """
    Model for creating a new product.

    Inherited from ProductBase, includes fields required for product creation.
    """
    pass

class ProductUpdate(ProductBase):
    """
    Model for updating product information.

    Inherited from ProductBase, includes fields for updating product details.
    """
    pass

class Product(ProductBase):
    """
    Model for retrieving product details.

    Inherited from ProductBase, includes fields for displaying product information.
    """
    product_id: int

    class Config:
        orm_mode = True

class CategoryBase(BaseModel):
    """
    Base model for product categories.

    Common fields for creating and updating product categories.
    """
    name: str

class CategoryCreate(CategoryBase):
    """
    Model for creating a new product category.

    Inherited from CategoryBase, includes fields required for category creation.
    """
    pass

class Category(CategoryBase):
    """
    Model for retrieving product category details.

    Inherited from CategoryBase, includes fields for displaying category information.
    """
    category_id: int

    class Config:
        orm_mode = True

class CustomerServiceBase(BaseModel):
    """
    Base model for customer service inquiries.

    Common fields for creating and updating customer service inquiries.
    """
    user_id: int
    date: str
    message: str

class CustomerServiceCreate(CustomerServiceBase):
    """
    Model for creating a new customer service inquiry.

    Inherited from CustomerServiceBase, includes fields required for inquiry creation.
    """
    pass

class CustomerService(CustomerServiceBase):
    """
    Model for retrieving customer service inquiry details.

    Inherited from CustomerServiceBase, includes fields for displaying inquiry information.
    """
    inquiry_id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    """
    Model for an access token.

    Includes fields for access token and token type.
    """
    access_token: str
    token_type: str
