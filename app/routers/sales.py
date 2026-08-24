from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.sale import create_sale, get_sale, get_sale_items, get_sales
from app.database import get_db
from app.schemas.sale import SaleCreate, SaleResponse

router = APIRouter(prefix="/sales", tags=["Sales"])


def sale_response(sale, db):
	return {
		"id": sale.id,
		"customer_id": sale.customer_id,
		"total_amount": sale.total_amount,
		"items": get_sale_items(db, sale.id)
	}


@router.post("/", response_model=SaleResponse)
def create_bill(data: SaleCreate, db: Session = Depends(get_db)):
	return sale_response(create_sale(db, data), db)


@router.get("/", response_model=list[SaleResponse])
def view_sales(db: Session = Depends(get_db)):
	return [sale_response(sale, db) for sale in get_sales(db)]


@router.get("/{sale_id}", response_model=SaleResponse)
def view_sale(sale_id: int, db: Session = Depends(get_db)):
	sale = get_sale(db, sale_id)
	if not sale:
		raise HTTPException(404, "Sale not found")
	return sale_response(sale, db)
