from sqlalchemy.orm import Session

from app.crud.category import (
    create_category,
    get_categories,
    get_category,
    update_category,
    delete_category
)
from app.schemas.category import (
    CategoryCreate,
    CategoryUpdate
)


def create_category_service(
    db: Session,
    category: CategoryCreate
):
    return create_category(
        db,
        category
    )


def get_categories_service(
    db: Session
):
    return get_categories(db)


def get_category_service(
    db: Session,
    category_id: int
):
    return get_category(
        db,
        category_id
    )


def update_category_service(
    db: Session,
    category_id: int,
    category: CategoryUpdate
):
    return update_category(
        db,
        category_id,
        category
    )


def delete_category_service(
    db: Session,
    category_id: int
):
    return delete_category(
        db,
        category_id
    )