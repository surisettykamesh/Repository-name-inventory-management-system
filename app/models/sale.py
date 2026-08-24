from sqlalchemy import Column, DateTime, Float, Integer, text

from app.database import Base


class Sale(Base):
	__tablename__ = "sales"

	id = Column(Integer, primary_key=True, index=True)
	customer_id = Column(Integer, nullable=True)
	total_amount = Column(Float, nullable=False, default=0)
	created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
