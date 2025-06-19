from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "uuid": "123e4567-e89b-12d3-a456-426614174000",
                "username": "john_doe",
                "email": "johndoe@example.com",
                "full_name": "John Doe",
                "bio": "Avid wine enthusiast and connoisseur."
            }
        })
    
    id: int
    uuid: str
    username: str
    email: str
    full_name: str
    bio: str = ""
    