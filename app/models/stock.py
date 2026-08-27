from sqlalchemy import Column, Integer, DateTime, ForeignKey, func

from app.database import Base


class Stock(Base):
    __tablename__ = "stock"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id", ondelete="CASCADE"),
        nullable=False,
        unique=True
    )

    quantity = Column(
        Integer,
        nullable=False,
        default=0
    )

    low_stock_limit = Column(
        Integer,
        nullable=False,
        default=10
    )

    last_updated = Column(
        DateTime,
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp()
    )
