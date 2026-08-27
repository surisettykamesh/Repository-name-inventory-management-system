from datetime import date, datetime, time

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.sale import Sale
from app.models.sale_item import SaleItem
from app.models.product import Product


def get_daily_sales(db: Session, report_date: date):
    start_datetime = datetime.combine(report_date, time.min)
    end_datetime = datetime.combine(report_date, time.max)

    result = db.query(
        func.count(Sale.id).label("total_bills"),
        func.coalesce(func.sum(Sale.total_amount), 0).label("total_sales")
    ).filter(
        Sale.created_at >= start_datetime,
        Sale.created_at <= end_datetime
    ).first()

    return {
        "date": report_date,
        "total_bills": result.total_bills,
        "total_sales": float(result.total_sales)
    }


def get_total_revenue(db: Session):
    result = db.query(
        func.coalesce(func.sum(Sale.total_amount), 0).label("total_revenue")
    ).first()

    return {
        "total_revenue": float(result.total_revenue)
    }


def get_product_sales(db: Session):
    results = db.query(
        Product.id.label("product_id"),
        Product.name.label("product_name"),
        func.coalesce(func.sum(SaleItem.quantity), 0).label("quantity_sold"),
        func.coalesce(func.sum(SaleItem.total_price), 0).label("revenue")
    ).join(
        SaleItem,
        Product.id == SaleItem.product_id
    ).group_by(
        Product.id,
        Product.name
    ).all()

    return [
        {
            "product_id": row.product_id,
            "product_name": row.product_name,
            "quantity_sold": row.quantity_sold,
            "revenue": float(row.revenue)
        }
        for row in results
    ]