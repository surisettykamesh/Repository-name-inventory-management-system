from fastapi import FastAPI
from sqlalchemy import text

from app.database import engine
from app.database import Base
from app.models.category import Category
from app.models.customer import Customer
from app.models.product import Product
from app.models.sale import Sale
from app.models.sale_item import SaleItem
from app.models.stock import Stock
from app.models.supplier import Supplier
from app.routers.category import router as category_router
from app.routers.customer import router as customer_router
from app.routers.product import router as product_router
from app.routers.reports import router as reports_router
from app.routers.sales import router as sales_router
from app.routers.stock import router as stock_router
from app.routers.supplier import router as supplier_router


app = FastAPI(
    title="Inventory Management System",
    description="Inventory Management System API",
    version="1.0.0"
)



app.include_router(category_router)
app.include_router(customer_router)
app.include_router(product_router)
app.include_router(supplier_router)
app.include_router(stock_router)
app.include_router(sales_router)
app.include_router(reports_router)

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "message": "Inventory Management System API is running"
    }


@app.get("/test-db")
def test_database():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))

            return {
                "message": "Database connected successfully",
                "result": result.scalar()
            }

    except Exception as e:
        return {
            "message": "Database connection failed",
            "error": str(e)
        }