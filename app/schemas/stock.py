from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict


class StockCreate(BaseModel):
    product_id: int = Field(..., gt=0)
    quantity: int = Field(default=0, ge=0)
    low_stock_limit: int = Field(default=10, ge=0)


class StockUpdate(BaseModel):
    quantity: int = Field(..., ge=0)
    low_stock_limit: int = Field(..., ge=0)


class StockAdd(BaseModel):
    quantity: int = Field(..., gt=0)


class StockReduce(BaseModel):
    quantity: int = Field(..., gt=0)


class StockResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    low_stock_limit: int
    last_updated: datetime

    model_config = ConfigDict(from_attributes=True)


class LowStockResponse(BaseModel):
    product_id: int
    product_name: str
    quantity: int
    low_stock_limit: int
    status: str
