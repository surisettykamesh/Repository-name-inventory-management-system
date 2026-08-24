from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.sale import Sale
from app.models.sale_item import SaleItem
from app.schemas.sale import SaleCreate


def create_sale(db: Session, data: SaleCreate):
	total = sum(item.quantity * item.unit_price for item in data.items)
	sale = Sale(customer_id=data.customer_id, total_amount=total)
	db.add(sale)
	db.flush()
	for item in data.items:
		db.add(SaleItem(
			sale_id=sale.id,
			product_id=item.product_id,
			quantity=item.quantity,
			unit_price=item.unit_price,
			total_price=item.quantity * item.unit_price
		))
	db.commit()
	db.refresh(sale)
	return sale


def get_sales(db: Session):
	return db.query(Sale).all()


def get_sale(db: Session, sale_id: int):
	return db.query(Sale).filter(Sale.id == sale_id).first()


def get_sale_items(db: Session, sale_id: int):
	return db.query(SaleItem).filter(SaleItem.sale_id == sale_id).all()


def daily_sales(db: Session):
	rows = db.query(
		func.date(Sale.created_at).label("date"),
		func.count(Sale.id).label("sales_count"),
		func.sum(Sale.total_amount).label("revenue")
	).group_by(func.date(Sale.created_at)).all()
	return [{"date": str(row.date), "sales_count": row.sales_count, "revenue": float(row.revenue or 0)} for row in rows]


def product_sales_summary(db: Session):
	rows = db.query(
		SaleItem.product_id,
		func.sum(SaleItem.quantity).label("quantity_sold"),
		func.sum(SaleItem.total_price).label("revenue")
	).group_by(SaleItem.product_id).all()
	return [{"product_id": row.product_id, "quantity_sold": row.quantity_sold, "revenue": float(row.revenue or 0)} for row in rows]
