from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.stock import Stock
from app.models.product import Product


def create_stock(
    db: Session,
    product_id: int,
    quantity: int,
    low_stock_limit: int
):
    # Check product exists
    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if not product:
        raise HTTPException(
            status_code=400,
            detail="Product not found"
        )

    # Check stock already exists for this product
    existing_stock = (
        db.query(Stock)
        .filter(Stock.product_id == product_id)
        .first()
    )

    if existing_stock:
        raise HTTPException(
            status_code=400,
            detail="Stock already exists for this product"
        )

    # Create stock
    stock = Stock(
        product_id=product_id,
        quantity=quantity,
        low_stock_limit=low_stock_limit
    )

    db.add(stock)
    db.commit()
    db.refresh(stock)

    return stock


def get_all_stock(db: Session):
    return db.query(Stock).all()


def get_stock_by_id(db: Session, stock_id: int):
    stock = (
        db.query(Stock)
        .filter(Stock.id == stock_id)
        .first()
    )

    if not stock:
        raise HTTPException(
            status_code=404,
            detail="Stock not found"
        )

    return stock


def update_stock(
    db: Session,
    stock_id: int,
    quantity: int,
    low_stock_limit: int
):
    stock = get_stock_by_id(db, stock_id)

    stock.quantity = quantity
    stock.low_stock_limit = low_stock_limit

    db.commit()
    db.refresh(stock)

    return stock


def add_stock(
    db: Session,
    stock_id: int,
    quantity: int
):
    stock = get_stock_by_id(db, stock_id)

    stock.quantity += quantity

    db.commit()
    db.refresh(stock)

    return stock


def reduce_stock(
    db: Session,
    stock_id: int,
    quantity: int
):
    stock = get_stock_by_id(db, stock_id)

    if quantity > stock.quantity:
        raise HTTPException(
            status_code=400,
            detail="Insufficient stock"
        )

    stock.quantity -= quantity

    db.commit()
    db.refresh(stock)

    return stock


def get_low_stock(db: Session):
    return (
        db.query(Stock)
        .filter(Stock.quantity <= Stock.low_stock_limit)
        .all()
    )


def delete_stock(db: Session, stock_id: int):
    stock = get_stock_by_id(db, stock_id)

    db.delete(stock)
    db.commit()

    return {
        "message": "Stock deleted successfully"
    }
