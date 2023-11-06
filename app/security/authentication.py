from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, status, Depends
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from typing import Annotated

from config import *
from app import crud, schema, models
from app.database import engine, get_db

# Create database tables if they don't exist
models.Base.metadata.create_all(bind=engine)

# Create a password context for hashing and verifying passwords
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Define the OAuth2 password bearer token scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    """
    Verify a plaintext password against a hashed password.

    Args:
        plain_password (str): The plaintext password.
        hashed_password (str): The hashed password.

    Returns:
        bool: True if the passwords match, False otherwise.
    """
    return password_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    """
    Hash a password using a password context.

    Args:
        password (str): The password to be hashed.

    Returns:
        str: The hashed password.
    """
    return password_context.hash(password)

def authenticate_user(db: Session, username: str, password: str):
    """
    Authenticate a user with a username and password.

    Args:
        db (Session): The database session.
        username (str): The username of the user.
        password (str): The user's password.

    Returns:
        schema.User | bool: The authenticated user or False if authentication fails.
    """
    user = crud.get_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

def generate_access_token(user: schema.UserBase, expires_delta: timedelta | None = None):
    """
    Generate an access token for a user.

    Args:
        user (schema.UserBase): The user for whom the token is generated.
        expires_delta (timedelta | None): The expiration time for the token.

    Returns:
        str: The generated access token.
    """
    to_encode = user.dict()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    """
    Get the current user based on the provided access token.

    Args:
        token (Annotated[str, Depends(oauth2_scheme)]): The access token for authentication.
        db (Session): The database session.

    Returns:
        schema.User: The authenticated user.

    Raises:
        HTTPException: If the token is invalid or the user is not found.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schema.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = crud.get_user_by_username(db, token_data.username)
    if user is None:
        raise credentials_exception
    return user
