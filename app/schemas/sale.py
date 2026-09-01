from pydantic import BaseModel, Field

from app.schemas.sale_item import (
    SaleItemCreate,
    SaleItemResponse
)


class SaleCreate(BaseModel):
    customer_id: int | None = Field(
        default=None,
        gt=0
    )

    items: list[SaleItemCreate] = Field(
        ...,
        min_length=1
    )


class SaleResponse(BaseModel):
    id: int
    customer_id: int | None
    total_amount: float
    items: list[SaleItemResponse] = Field(
        default_factory=list
    )

    class Config:
        from_attributes = True