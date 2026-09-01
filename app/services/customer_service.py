from sqlalchemy.orm import Session

from app.crud.customer import (
    create_customer,
    get_customers,
    get_customer,
    update_customer,
    delete_customer
)

from app.schemas.customer import (
    CustomerCreate,
    CustomerUpdate
)


def create_customer_service(
    db: Session,
    customer: CustomerCreate
):
    return create_customer(
        db,
        customer
    )


def get_customers_service(
    db: Session
):
    return get_customers(db)


def get_customer_service(
    db: Session,
    customer_id: int
):
    return get_customer(
        db,
        customer_id
    )


def update_customer_service(
    db: Session,
    customer_id: int,
    customer: CustomerUpdate
):
    return update_customer(
        db,
        customer_id,
        customer
    )


def delete_customer_service(
    db: Session,
    customer_id: int
):
    return delete_customer(
        db,
        customer_id
    )