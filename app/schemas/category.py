from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
	name: str = Field(
		...,
		min_length=2,
		max_length=100
	)

	description: str | None = None


class CategoryCreate(CategoryBase):
	pass


class CategoryUpdate(BaseModel):
	name: str | None = Field(
		default=None,
		min_length=2,
		max_length=100
	)

	description: str | None = None


class CategoryResponse(CategoryBase):
	id: int

	class Config:
		from_attributes = True
