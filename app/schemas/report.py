from pydantic import BaseModel
from datetime import date


class DailySalesReport(BaseModel):
    date: date
    total_bills: int
    total_sales: float


class RevenueReport(BaseModel):
    total_revenue: float


class ProductSalesReport(BaseModel):
    product_id: int
    product_name: str
    quantity_sold: int
    revenue: float