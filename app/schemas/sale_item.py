from pydantic import BaseModel, Field


class SaleItemCreate(BaseModel):
    product_id: int = Field(..., gt=0)
    quantity: int = Field(..., gt=0)


class SaleItemResponse(BaseModel):
    id: int
    sale_id: int
    product_id: int
    quantity: int
    unit_price: float
    total_price: float

    class Config:
        from_attributes = True