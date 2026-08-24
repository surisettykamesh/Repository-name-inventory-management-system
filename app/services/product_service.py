from sqlalchemy.orm import Session

from app.crud import product as product_crud
from app.schemas.product import ProductCreate, ProductUpdate


def create_product(
    db: Session,
    product: ProductCreate
):
    return product_crud.create_product(
        db,
        product
    )


def get_products(
    db: Session
):
    return product_crud.get_products(db)


def get_product(
    db: Session,
    product_id: int
):
    return product_crud.get_product(
        db,
        product_id
    )


def update_product(
    db: Session,
    product_id: int,
    product: ProductUpdate
):
    return product_crud.update_product(
        db,
        product_id,
        product
    )


def delete_product(
    db: Session,
    product_id: int
):
    return product_crud.delete_product(
        db,
        product_id
    )
