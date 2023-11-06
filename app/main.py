from fastapi import Depends, FastAPI
from config import DEBUG

# Updated import paths for routers
from app.routers import cart, products, orders, inquiries, items, token, users

app = FastAPI(
    debug=DEBUG,
    title="FastAPI Demo",
    description="A demo of the FastAPI framework",
    version="1.0.0"
)

# Documentation for the overall FastAPI app
"""
This FastAPI application serves as the backend for your project. It includes various routers
to handle different parts of the application.
"""

# Include routers with descriptions
app.include_router(products.router)
"""
Router for managing product-related endpoints.

- prefix: /products
- tags: Products
"""

app.include_router(cart.router)
"""
Router for managing shopping cart-related endpoints.

- prefix: /cart
- tags: Cart
"""

app.include_router(orders.router)
"""
Router for managing order-related endpoints.

- prefix: /orders
- tags: Orders
"""

app.include_router(inquiries.router)
"""
Router for handling inquiries and support-related endpoints.

- prefix: /inquiries
- tags: Inquiries
"""

app.include_router(items.router)
"""
Router for managing item-related endpoints.

- prefix: /items
- tags: Items
"""

app.include_router(token.router)
"""
Router for handling authentication and token-related endpoints.

- prefix: /token
- tags: Token
"""
