from sqlalchemy import Column, Float, ForeignKey, Integer

from app.database import Base


class SaleItem(Base):
	__tablename__ = "sale_items"

	id = Column(Integer, primary_key=True, index=True)
	sale_id = Column(Integer, ForeignKey("sales.id"), nullable=False)
	product_id = Column(Integer, nullable=False)
	quantity = Column(Integer, nullable=False)
	unit_price = Column(Float, nullable=False)
	total_price = Column(Float, nullable=False)
