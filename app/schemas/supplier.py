from pydantic import BaseModel, EmailStr


class SupplierBase(BaseModel):
	name: str
	contact: str
	email: EmailStr | None = None
	address: str | None = None


class SupplierCreate(SupplierBase):
	pass


class SupplierUpdate(BaseModel):
	name: str | None = None
	contact: str | None = None
	email: EmailStr | None = None
	address: str | None = None


class SupplierResponse(SupplierBase):
	id: int

	class Config:
		from_attributes = True
