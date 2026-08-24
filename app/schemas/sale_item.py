from pydantic import BaseModel, Field


class SaleItemCreate(BaseModel):
	product_id: int = Field(..., gt=0)
	quantity: int = Field(..., gt=0)
	unit_price: float = Field(..., gt=0)


class SaleItemResponse(SaleItemCreate):
	id: int
	sale_id: int
	total_price: float

	class Config:
		from_attributes = True
