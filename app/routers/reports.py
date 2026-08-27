from datetime import date

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.report import (
    DailySalesReport,
    RevenueReport,
    ProductSalesReport,
)
from app.services.report_service import (
    daily_sales_report,
    total_revenue_report,
    product_sales_report,
)

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get("/daily-sales", response_model=DailySalesReport)
def daily_sales(
    report_date: date = Query(..., description="Enter the report date"),
    db: Session = Depends(get_db)
):
    return daily_sales_report(db, report_date)


@router.get("/revenue", response_model=RevenueReport)
def total_revenue(
    db: Session = Depends(get_db)
):
    return total_revenue_report(db)


@router.get("/product-sales", response_model=list[ProductSalesReport])
def product_sales(
    db: Session = Depends(get_db)
):
    return product_sales_report(db)