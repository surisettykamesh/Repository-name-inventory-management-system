from sqlalchemy import Column, DateTime, Integer, text

from app.database import Base


class Stock(Base):
	__tablename__ = "stock"

	id = Column(Integer, primary_key=True, index=True)
	product_id = Column(Integer, nullable=False, index=True)
	quantity = Column(Integer, nullable=False, default=0)
	updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
