from pydantic import BaseModel, ConfigDict, field_validator
from typing import Optional
from src.config.settings import Settings


class Rating(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "uuid": "123e4567-e89b-12d3-a456-426614174000",
                "object_id": 101,
                "object_type": "wine",
                "user_id": 42,
                "rating": 4.5,
                "comment": "A delightful wine with a smooth finish."
            }
        })
    
    id: int
    uuid: str
    object_id: int
    object_type: str  # e.g., "wine", "beer", etc.
    user_id: int
    rating: float
    comment: Optional[str] = ""
    
    @field_validator('rating', mode='before')
    @classmethod
    def validate_rating(cls, value):
        if not (0 <= value <= 5):
            raise ValueError("Rating must be between 0 and 5")
        return round(value, 2)  # Round rating to 2 decimal places
    
    @field_validator('object_type', mode='before')
    @classmethod
    def validate_object_type(cls, value):
        rating_types = Settings.RATING_TYPES
        if value not in rating_types:
            raise ValueError(f"Object type must be one of {rating_types}")
        return value.lower()  # Normalize to lowercase for consistency
