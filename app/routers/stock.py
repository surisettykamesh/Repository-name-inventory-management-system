from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.stock import create_stock, delete_stock, get_stock, get_stock_records, update_stock
from app.database import get_db
from app.schemas.stock import StockCreate, StockResponse, StockUpdate

router = APIRouter(prefix="/stock", tags=["Stock"])


@router.post("/", response_model=StockResponse)
def add_stock(data: StockCreate, db: Session = Depends(get_db)):
	return create_stock(db, data)


@router.get("/", response_model=list[StockResponse])
def view_stock(db: Session = Depends(get_db)):
	return get_stock_records(db)


@router.get("/low", response_model=list[StockResponse])
def view_low_stock(threshold: int = 10, db: Session = Depends(get_db)):
	return [item for item in get_stock_records(db) if item.quantity <= threshold]


@router.put("/{stock_id}", response_model=StockResponse)
def edit_stock(stock_id: int, data: StockUpdate, db: Session = Depends(get_db)):
	stock = update_stock(db, stock_id, data)
	if not stock:
		raise HTTPException(404, "Stock record not found")
	return stock


@router.delete("/{stock_id}")
def remove_stock(stock_id: int, db: Session = Depends(get_db)):
	if not delete_stock(db, stock_id):
		raise HTTPException(404, "Stock record not found")
	return {"message": "Stock record deleted successfully"}
