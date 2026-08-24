from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.supplier import create_supplier, delete_supplier, get_supplier, get_suppliers, update_supplier
from app.database import get_db
from app.schemas.supplier import SupplierCreate, SupplierResponse, SupplierUpdate

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])


@router.post("/", response_model=SupplierResponse)
def add_supplier(data: SupplierCreate, db: Session = Depends(get_db)):
	return create_supplier(db, data)


@router.get("/", response_model=list[SupplierResponse])
def view_suppliers(db: Session = Depends(get_db)):
	return get_suppliers(db)


@router.get("/{supplier_id}", response_model=SupplierResponse)
def view_supplier(supplier_id: int, db: Session = Depends(get_db)):
	supplier = get_supplier(db, supplier_id)
	if not supplier:
		raise HTTPException(404, "Supplier not found")
	return supplier


@router.put("/{supplier_id}", response_model=SupplierResponse)
def edit_supplier(supplier_id: int, data: SupplierUpdate, db: Session = Depends(get_db)):
	supplier = update_supplier(db, supplier_id, data)
	if not supplier:
		raise HTTPException(404, "Supplier not found")
	return supplier


@router.delete("/{supplier_id}")
def remove_supplier(supplier_id: int, db: Session = Depends(get_db)):
	if not delete_supplier(db, supplier_id):
		raise HTTPException(404, "Supplier not found")
	return {"message": "Supplier deleted successfully"}
