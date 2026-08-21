from fastapi import FastAPI

app = FastAPI(
    title="Inventory Management System",
    description="Backend API for Inventory and Sales Management",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Inventory Management System API is running"
    }