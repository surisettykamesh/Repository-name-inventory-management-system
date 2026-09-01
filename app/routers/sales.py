from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.sale import (
    SaleCreate,
    SaleResponse
)

from app.services.sales_service import (
    create_sale_service,
    get_sales_service,
    get_sale_service,
    get_sale_items_service
)


router = APIRouter(
    prefix="/sales",
    tags=["Sales"]
)


def sale_response(
    sale,
    db: Session
):
    return {
        "id": sale.id,
        "customer_id": sale.customer_id,
        "total_amount": sale.total_amount,
        "items": get_sale_items_service(
            db,
            sale.id
        )
    }


@router.post(
    "/",
    response_model=SaleResponse
)
def create_bill(
    data: SaleCreate,
    db: Session = Depends(get_db)
):
    sale = create_sale_service(
        db,
        data
    )

    return sale_response(
        sale,
        db
    )


@router.get(
    "/",
    response_model=list[SaleResponse]
)
def view_sales(
    db: Session = Depends(get_db)
):
    sales = get_sales_service(db)

    return [
        sale_response(
            sale,
            db
        )
        for sale in sales
    ]


@router.get(
    "/{sale_id}",
    response_model=SaleResponse
)
def view_sale(
    sale_id: int,
    db: Session = Depends(get_db)
):
    sale = get_sale_service(
        db,
        sale_id
    )

    if not sale:
        raise HTTPException(
            status_code=404,
            detail="Sale not found"
        )

    return sale_response(
        sale,
        db
    )