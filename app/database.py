from fastapi import FastAPI
from sqlalchemy import text

from app.database import engine


app = FastAPI(
    title="Inventory Management System",
    description="Inventory Management System API",
    version="1.0.0"
)


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