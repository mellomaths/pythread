from pydantic import BaseModel, ConfigDict


class Wine(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "uuid": "123e4567-e89b-12d3-a456-426614174000",
                "name": "Chardonnay",
                "description": "A full-bodied white wine with notes of apple and pear.",
                "country": "France",
                "variety": "Chardonnay",
                "year": 2019,
                "type": "white",
                "price": 15.99
            }
        })
    
    id: int
    uuid: str
    name: str
    description: str
    country: str
    variety: str
    year: int
    type: str
    price: float
