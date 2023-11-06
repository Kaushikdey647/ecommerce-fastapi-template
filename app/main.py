from datetime import timedelta
from typing import Annotated
from config import ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app import schema
from app.database import engine, get_db
from app.security.authentication import password_context, oauth2_scheme
from app.security.authentication import verify_password, get_password_hash, authenticate_user, generate_access_token, get_current_user
from app import crud

# Updated import paths for routers
from app.routers import cart, products, orders, inquiries, items, token, users

app = FastAPI(debug=True)


app.include_router(products.router)
app.include_router(cart.router)
app.include_router(orders.router)
app.include_router(inquiries.router)
app.include_router(items.router)
app.include_router(token.router)