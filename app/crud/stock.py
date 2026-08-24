from sqlalchemy.orm import Session

from app.models.stock import Stock
from app.schemas.stock import StockCreate, StockUpdate


def create_stock(db: Session, data: StockCreate):
	stock = Stock(**data.model_dump())
	db.add(stock)
	db.commit()
	db.refresh(stock)
	return stock


def get_stock_records(db: Session):
	return db.query(Stock).all()


def get_stock(db: Session, stock_id: int):
	return db.query(Stock).filter(Stock.id == stock_id).first()


def update_stock(db: Session, stock_id: int, data: StockUpdate):
	stock = get_stock(db, stock_id)
	if not stock:
		return None
	stock.quantity = data.quantity
	db.commit()
	db.refresh(stock)
	return stock


def delete_stock(db: Session, stock_id: int):
	stock = get_stock(db, stock_id)
	if not stock:
		return None
	db.delete(stock)
	db.commit()
	return stock
