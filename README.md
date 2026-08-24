# Inventory Management System API

A FastAPI backend for supermarket inventory management.

## Current Status

The API starts with Uvicorn and exposes home, database-check, category, customer, product, supplier, stock, sales, and reports routes. Category CRUD is the module contributed by **Surisetty Kamesh** for this project.

The default development database is a local SQLite file named `inventory.db`, created automatically at startup. Set the `DATABASE_URL` environment variable to use MySQL or another SQLAlchemy database.

## Requirements

- Python 3.13 or compatible Python 3 version
- SQLite for the default setup
- MySQL Server and a `supermarket_db` database when using `DATABASE_URL`

## Installation

From the repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the API

Run this command from the repository root, the directory containing the `app` folder:

```powershell
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

The API is available at:

- http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- OpenAPI JSON: http://127.0.0.1:8000/openapi.json

## Database Setup

The default setup needs no database command. Starting the app creates `inventory.db` and all model tables automatically.

To use MySQL instead, set the connection URL before starting the app:

```powershell
$env:DATABASE_URL = "mysql+pymysql://USERNAME:PASSWORD@localhost:3306/supermarket_db"
```

Create the database in MySQL first if needed:

```sql
CREATE DATABASE supermarket_db;
```

The `/test-db` endpoint reports whether the active connection works:

```text
GET http://127.0.0.1:8000/test-db
```

Tables are created by the database setup used by the project when models are initialized. If a table is missing, create the required tables before calling category or customer CRUD endpoints.

## Implemented Endpoints

### Categories

- `POST /categories/` - add a category
- `GET /categories/` - view all categories
- `GET /categories/{category_id}` - view one category
- `PUT /categories/{category_id}` - update a category
- `DELETE /categories/{category_id}` - delete a category

Category request example:

```json
{
  "name": "Fresh Food",
  "description": "Fruit, vegetables, and other fresh items"
}
```

### Customers

- `POST /customers/` - add a customer
- `GET /customers/` - view all customers
- `GET /customers/{customer_id}` - view one customer
- `PUT /customers/{customer_id}` - update a customer
- `DELETE /customers/{customer_id}` - delete a customer

### Products

- `POST /products/` - add a product
- `GET /products/` - view all products
- `GET /products/{product_id}` - view one product
- `PUT /products/{product_id}` - update a product
- `DELETE /products/{product_id}` - delete a product

### Suppliers

- `POST /suppliers/` - add a supplier
- `GET /suppliers/` - view all suppliers
- `GET /suppliers/{supplier_id}` - view one supplier
- `PUT /suppliers/{supplier_id}` - update a supplier
- `DELETE /suppliers/{supplier_id}` - delete a supplier

### Stock

- `POST /stock/` - create a stock record
- `GET /stock/` - view stock
- `GET /stock/low?threshold=10` - view low-stock records
- `PUT /stock/{stock_id}` - update stock quantity
- `DELETE /stock/{stock_id}` - delete a stock record

### Sales and Reports

- `POST /sales/` - create a bill and calculate its total
- `GET /sales/` - view sales
- `GET /sales/{sale_id}` - view one sale
- `GET /reports/daily-sales` - daily sales and revenue
- `GET /reports/product-sales` - product sales summary

### General

- `GET /` - API health message
- `GET /test-db` - database connectivity check

## Postman

Import `postman/inventory-management-system.postman_collection.json` into Postman. Set the collection variable `baseUrl` to `http://127.0.0.1:8000` when running locally.

The collection includes health checks, category CRUD, product, supplier, stock, sales, and report requests.

## Contribution

**Surisetty Kamesh**

- Set up the FastAPI project structure and common application configuration.
- Implemented the Categories module: SQLAlchemy model, Pydantic schemas, CRUD persistence functions, and FastAPI routes for add, view, update, and delete operations.
- Registered the category router in the main application.
- Added the dependency manifest, API documentation, and Postman collection for local testing.
- Added automatic local SQLite setup so the API can run without a separate MySQL installation.
