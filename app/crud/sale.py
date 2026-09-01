from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.sale import Sale
from app.models.sale_item import SaleItem
from app.models.product import Product
from app.models.stock import Stock
from app.models.customer import Customer
from app.schemas.sale import SaleCreate


def create_sale(db: Session, data: SaleCreate):
    try:
        # Check customer if customer_id is provided
        if data.customer_id is not None:
            customer = (
                db.query(Customer)
                .filter(Customer.id == data.customer_id)
                .first()
            )

            if not customer:
                raise ValueError("Customer not found")

        total = 0

        sale_items = []

        for item in data.items:

            # Get product
            product = (
                db.query(Product)
                .filter(Product.id == item.product_id)
                .first()
            )

            if not product:
                raise ValueError(
                    f"Product {item.product_id} not found"
                )

            # Check product quantity
            if product.quantity < item.quantity:
                raise ValueError(
                    f"Insufficient stock for product "
                    f"{product.name}"
                )

            # Get stock record
            stock = (
                db.query(Stock)
                .filter(
                    Stock.product_id == item.product_id
                )
                .first()
            )

            # Use product price from database
            unit_price = product.price

            item_total = unit_price * item.quantity

            total += item_total

            # Reduce product quantity
            product.quantity -= item.quantity

            # Reduce stock quantity if stock exists
            if stock:
                stock.quantity -= item.quantity

            sale_items.append(
                {
                    "product_id": item.product_id,
                    "quantity": item.quantity,
                    "unit_price": unit_price,
                    "total_price": item_total
                }
            )

        # Create sale
        sale = Sale(
            customer_id=data.customer_id,
            total_amount=total
        )

        db.add(sale)

        # Generate sale ID before creating items
        db.flush()

        # Create sale items
        for item in sale_items:
            db.add(
                SaleItem(
                    sale_id=sale.id,
                    product_id=item["product_id"],
                    quantity=item["quantity"],
                    unit_price=item["unit_price"],
                    total_price=item["total_price"]
                )
            )

        db.commit()

        db.refresh(sale)

        return sale

    except Exception:
        db.rollback()
        raise


def get_sales(db: Session):
    return (
        db.query(Sale)
        .order_by(Sale.id.desc())
        .all()
    )


def get_sale(db: Session, sale_id: int):
    return (
        db.query(Sale)
        .filter(Sale.id == sale_id)
        .first()
    )


def get_sale_items(db: Session, sale_id: int):
    return (
        db.query(SaleItem)
        .filter(SaleItem.sale_id == sale_id)
        .all()
    )


def daily_sales(db: Session):
    rows = (
        db.query(
            func.date(Sale.created_at).label("date"),
            func.count(Sale.id).label("sales_count"),
            func.sum(Sale.total_amount).label("revenue")
        )
        .group_by(
            func.date(Sale.created_at)
        )
        .all()
    )

    return [
        {
            "date": str(row.date),
            "sales_count": row.sales_count,
            "revenue": float(row.revenue or 0)
        }
        for row in rows
    ]


def product_sales_summary(db: Session):
    rows = (
        db.query(
            SaleItem.product_id,
            func.sum(
                SaleItem.quantity
            ).label("quantity_sold"),
            func.sum(
                SaleItem.total_price
            ).label("revenue")
        )
        .group_by(
            SaleItem.product_id
        )
        .all()
    )

    return [
        {
            "product_id": row.product_id,
            "quantity_sold": row.quantity_sold,
            "revenue": float(row.revenue or 0)
        }
        for row in rows
    ]