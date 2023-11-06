from fastapi import APIRouter, Depends
from app import schema
from app.security.authentication import get_current_user
from app import crud
from app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/users/me/", response_model=schema.User)
async def read_users_me(current_user: schema.User = Depends(get_current_user)):
    return current_user

@router.post("/users/", response_model=schema.User)
async def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db=db, user=user)
    return db_user