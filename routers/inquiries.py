from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schema

from database import get_db

router = APIRouter(
    prefix="/inquiries",
    responses={404: {"description": "Not found"}}
)

@router.get("/api/inquiries", response_model=list[schema.CustomerService])
def read_inquiries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    inquiries = crud.get_inquiries_list(db, skip=skip, limit=limit)
    return inquiries

@router.post("/api/inquiries", response_model=schema.CustomerService)
def create_inquiry(inquiry: schema.CustomerServiceCreate, db: Session = Depends(get_db)):
    db_inquiry = crud.add_inquiry(db, inquiry=inquiry)
    return db_inquiry

@router.get("/api/inquiries/{inquiry_id}", response_model=schema.CustomerService)
def read_inquiry(inquiry_id: int, db: Session = Depends(get_db)):
    db_inquiry = crud.get_inquiry_by_id(db, inquiry_id=inquiry_id)
    if db_inquiry is None:
        raise HTTPException(status_code=404, detail="Inquiry not found")
    return db_inquiry