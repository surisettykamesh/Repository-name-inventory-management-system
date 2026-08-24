from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.sale import daily_sales, product_sales_summary
from app.database import get_db
from app.schemas.report import DailySalesReport, ProductSalesSummary

router = APIRouter(prefix="/reports", tags=["Reports"])


@router.get("/daily-sales", response_model=list[DailySalesReport])
def get_daily_sales(db: Session = Depends(get_db)):
	return daily_sales(db)


@router.get("/product-sales", response_model=list[ProductSalesSummary])
def get_product_sales(db: Session = Depends(get_db)):
	return product_sales_summary(db)
