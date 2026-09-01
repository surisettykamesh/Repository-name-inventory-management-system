from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.customer import (
    CustomerCreate,
    CustomerUpdate,
    CustomerResponse
)

from app.services.customer_service import (
    create_customer_service,
    get_customers_service,
    get_customer_service,
    update_customer_service,
    delete_customer_service
)


router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.post(
    "/",
    response_model=CustomerResponse
)
def add_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):
    return create_customer_service(
        db,
        customer
    )


@router.get(
    "/",
    response_model=list[CustomerResponse]
)
def view_customers(
    db: Session = Depends(get_db)
):
    return get_customers_service(db)


@router.get(
    "/{customer_id}",
    response_model=CustomerResponse
)
def view_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    customer = get_customer_service(
        db,
        customer_id
    )

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer


@router.put(
    "/{customer_id}",
    response_model=CustomerResponse
)
def update_customer_api(
    customer_id: int,
    customer: CustomerUpdate,
    db: Session = Depends(get_db)
):
    updated_customer = update_customer_service(
        db,
        customer_id,
        customer
    )

    if not updated_customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return updated_customer


@router.delete(
    "/{customer_id}"
)
def remove_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    deleted_customer = delete_customer_service(
        db,
        customer_id
    )

    if not deleted_customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return {
        "message": "Customer deleted successfully"
    }