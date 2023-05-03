from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schema

from database import get_db

router = APIRouter(
    prefix="/products",
    responses={404: {"description": "Not found"}}
)

@router.get("/", response_model=list[schema.Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_product_list(db, skip=skip, limit=limit)
    return products

@router.get("/{product_id}", response_model=schema.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_id(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.post("/", response_model=schema.Product)
def create_product(product: schema.ProductCreate, db: Session = Depends(get_db)):
    db_product = crud.add_product(db, product=product)
    return db_product

@router.put("/{product_id}", response_model=schema.Product)
def update_product(product_id: int, product: schema.ProductUpdate, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_id(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud.update_product(db=db, product=db_product, product_update=product)

@router.delete("/{product_id}", response_model=schema.Product)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_id(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud.delete_product(db=db, product_id=product_id)