from pydantic import BaseModel


class ServiceUp(BaseModel):
    database: bool


class HealthCheck(BaseModel):
    
    success: bool
    up: ServiceUp
    
    class Config:
        json_schema_extra = {
            "example": {
                "success": True,
                "up": {
                    "database": True
                }
            }
        }
        validate_assignment = True
        use_enum_values = True