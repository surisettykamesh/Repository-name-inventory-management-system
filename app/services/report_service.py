from datetime import date

from sqlalchemy.orm import Session

from app.crud.report import (
    get_daily_sales,
    get_total_revenue,
    get_product_sales,
)


def daily_sales_report(db: Session, report_date: date):
    return get_daily_sales(db, report_date)


def total_revenue_report(db: Session):
    return get_total_revenue(db)


def product_sales_report(db: Session):
    return get_product_sales(db)