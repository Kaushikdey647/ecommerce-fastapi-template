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
from app.routers import cart, products, orders, inquiries

app = FastAPI(debug=True)


app.include_router(products.router)
app.include_router(cart.router)
app.include_router(orders.router)
app.include_router(inquiries.router)

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}

@app.get("/token", response_model=schema.Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = generate_access_token(user, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me/", response_model=schema.User)
async def read_users_me(current_user: schema.User = Depends(get_current_user)):
    return current_user

@app.post("/users/", response_model=schema.User)
async def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db=db, user=user)
    return db_user