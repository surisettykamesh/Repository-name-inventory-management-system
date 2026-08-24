from pydantic import BaseModel


class DailySalesReport(BaseModel):
	date: str
	sales_count: int
	revenue: float


class ProductSalesSummary(BaseModel):
	product_id: int
	quantity_sold: int
	revenue: float
