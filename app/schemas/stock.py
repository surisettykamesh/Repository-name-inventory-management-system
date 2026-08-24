from pydantic import BaseModel, Field


class StockBase(BaseModel):
	product_id: int = Field(..., gt=0)
	quantity: int = Field(..., ge=0)


class StockCreate(StockBase):
	pass


class StockUpdate(BaseModel):
	quantity: int = Field(..., ge=0)


class StockResponse(StockBase):
	id: int

	class Config:
		from_attributes = True
