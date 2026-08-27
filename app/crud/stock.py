from sqlalchemy.orm import Session

from app.models.stock import Stock
from app.models.product import Product

from app.schemas.stock import (
    StockCreate,
    StockUpdate,
    StockAdd,
    StockReduce
)


def create_stock(db: Session, stock_data: StockCreate):
    product = (
        db.query(Product)
        .filter(Product.id == stock_data.product_id)
        .first()
    )

    if not product:
        raise ValueError("Product not found")

    existing_stock = (
        db.query(Stock)
        .filter(Stock.product_id == stock_data.product_id)
        .first()
    )

    if existing_stock:
        raise ValueError(
            "Stock already exists for this product"
        )

    stock = Stock(
        product_id=stock_data.product_id,
        quantity=stock_data.quantity,
        low_stock_limit=stock_data.low_stock_limit
    )

    # Keep product quantity synchronized
    product.quantity = stock_data.quantity

    db.add(stock)
    db.commit()
    db.refresh(stock)

    return stock


def get_all_stock(db: Session):
    return db.query(Stock).all()


def get_stock_by_id(db: Session, stock_id: int):
    return (
        db.query(Stock)
        .filter(Stock.id == stock_id)
        .first()
    )


def update_stock(
    db: Session,
    stock_id: int,
    stock_data: StockUpdate
):
    stock = get_stock_by_id(db, stock_id)

    if not stock:
        return None

    product = (
        db.query(Product)
        .filter(Product.id == stock.product_id)
        .first()
    )

    stock.quantity = stock_data.quantity
    stock.low_stock_limit = stock_data.low_stock_limit

    if product:
        product.quantity = stock_data.quantity

    db.commit()
    db.refresh(stock)

    return stock


def add_stock(
    db: Session,
    stock_id: int,
    stock_data: StockAdd
):
    stock = get_stock_by_id(db, stock_id)

    if not stock:
        return None

    product = (
        db.query(Product)
        .filter(Product.id == stock.product_id)
        .first()
    )

    stock.quantity += stock_data.quantity

    if product:
        product.quantity = stock.quantity

    db.commit()
    db.refresh(stock)

    return stock


def reduce_stock(
    db: Session,
    stock_id: int,
    stock_data: StockReduce
):
    stock = get_stock_by_id(db, stock_id)

    if not stock:
        return None

    if stock.quantity < stock_data.quantity:
        raise ValueError("Insufficient stock")

    product = (
        db.query(Product)
        .filter(Product.id == stock.product_id)
        .first()
    )

    stock.quantity -= stock_data.quantity

    if product:
        product.quantity = stock.quantity

    db.commit()
    db.refresh(stock)

    return stock


def delete_stock(db: Session, stock_id: int):
    stock = get_stock_by_id(db, stock_id)

    if not stock:
        return None

    db.delete(stock)
    db.commit()

    return stock


def get_low_stock(db: Session):
    results = (
        db.query(Stock, Product)
        .join(
            Product,
            Stock.product_id == Product.id
        )
        .filter(
            Stock.quantity <= Stock.low_stock_limit
        )
        .all()
    )

    low_stock_products = []

    for stock, product in results:

        if stock.quantity == 0:
            status = "OUT OF STOCK"
        else:
            status = "LOW STOCK"

        low_stock_products.append({
            "product_id": product.id,
            "product_name": product.name,
            "quantity": stock.quantity,
            "low_stock_limit": stock.low_stock_limit,
            "status": status
        })

    return low_stock_products
