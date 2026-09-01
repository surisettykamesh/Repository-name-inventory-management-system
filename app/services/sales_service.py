from sqlalchemy.orm import Session

from app.crud.sale import (
    create_sale,
    get_sales,
    get_sale,
    get_sale_items
)

from app.schemas.sale import SaleCreate


def create_sale_service(
    db: Session,
    data: SaleCreate
):
    return create_sale(
        db,
        data
    )


def get_sales_service(
    db: Session
):
    return get_sales(db)


def get_sale_service(
    db: Session,
    sale_id: int
):
    return get_sale(
        db,
        sale_id
    )


def get_sale_items_service(
    db: Session,
    sale_id: int
):
    return get_sale_items(
        db,
        sale_id
    )