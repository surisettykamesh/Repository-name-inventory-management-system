from sqlalchemy.orm import Session

from app import crud
from app.schemas.product import ProductCreate, ProductUpdate


def create_product(
    db: Session,
    product: ProductCreate
):
    return crud.product.create_product(
        db,
        product
    )


def get_products(
    db: Session
):
    return crud.product.get_products(db)


def get_product(
    db: Session,
    product_id: int
):
    return crud.product.get_product(
        db,
        product_id
    )


def update_product(
    db: Session,
    product_id: int,
    product: ProductUpdate
):
    return crud.product.update_product(
        db,
        product_id,
        product
    )


def delete_product(
    db: Session,
    product_id: int
):
    return crud.product.delete_product(
        db,
        product_id
    )
