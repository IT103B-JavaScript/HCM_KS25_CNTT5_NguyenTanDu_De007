from pydantic import BaseModel, ConfigDict, Field


class ApartmentCreate(BaseModel):
    apartment_code: str = Field(..., min_length=4, max_length=10)
    monthly_rent: float = Field(..., gt=0)
    apartment_type_id: int = Field(...)


class ApartmentTypeResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class ApartmentResponse(BaseModel):
    id: int
    apartment_code: str
    monthly_rent: float
    apartment_type: ApartmentTypeResponse

    model_config = ConfigDict(from_attributes=True)