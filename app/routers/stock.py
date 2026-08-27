from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.stock import (
    StockCreate,
    StockUpdate,
    StockAdd,
    StockReduce,
    StockResponse,
    LowStockResponse
)

from app.crud import stock as stock_crud


router = APIRouter(
    prefix="/stock",
    tags=["Stock Management"]
)


# Create Stock
@router.post(
    "/",
    response_model=StockResponse,
    status_code=201
)
def create_stock(
    stock_data: StockCreate,
    db: Session = Depends(get_db)
):
    try:
        return stock_crud.create_stock(
            db,
            stock_data
        )

    except ValueError as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# Get All Stock
@router.get(
    "/",
    response_model=list[StockResponse]
)
def get_all_stock(
    db: Session = Depends(get_db)
):
    return stock_crud.get_all_stock(db)


# Low Stock
@router.get(
    "/low-stock",
    response_model=list[LowStockResponse]
)
def get_low_stock(
    db: Session = Depends(get_db)
):
    return stock_crud.get_low_stock(db)


# Get Stock By ID
@router.get(
    "/{stock_id}",
    response_model=StockResponse
)
def get_stock(
    stock_id: int,
    db: Session = Depends(get_db)
):
    stock = stock_crud.get_stock_by_id(
        db,
        stock_id
    )

    if not stock:
        raise HTTPException(
            status_code=404,
            detail="Stock not found"
        )

    return stock


# Update Stock
@router.put(
    "/{stock_id}",
    response_model=StockResponse
)
def update_stock(
    stock_id: int,
    stock_data: StockUpdate,
    db: Session = Depends(get_db)
):
    stock = stock_crud.update_stock(
        db,
        stock_id,
        stock_data
    )

    if not stock:
        raise HTTPException(
            status_code=404,
            detail="Stock not found"
        )

    return stock


# Add Stock
@router.patch(
    "/{stock_id}/add",
    response_model=StockResponse
)
def add_stock(
    stock_id: int,
    stock_data: StockAdd,
    db: Session = Depends(get_db)
):
    stock = stock_crud.add_stock(
        db,
        stock_id,
        stock_data
    )

    if not stock:
        raise HTTPException(
            status_code=404,
            detail="Stock not found"
        )

    return stock


# Reduce Stock
@router.patch(
    "/{stock_id}/reduce",
    response_model=StockResponse
)
def reduce_stock(
    stock_id: int,
    stock_data: StockReduce,
    db: Session = Depends(get_db)
):
    try:
        stock = stock_crud.reduce_stock(
            db,
            stock_id,
            stock_data
        )

        if not stock:
            raise HTTPException(
                status_code=404,
                detail="Stock not found"
            )

        return stock

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# Delete Stock
@router.delete(
    "/{stock_id}"
)
def delete_stock(
    stock_id: int,
    db: Session = Depends(get_db)
):
    stock = stock_crud.delete_stock(
        db,
        stock_id
    )

    if not stock:
        raise HTTPException(
            status_code=404,
            detail="Stock not found"
        )

    return {
        "message": "Stock deleted successfully"
    }
