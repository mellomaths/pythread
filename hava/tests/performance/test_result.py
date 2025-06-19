from typing import Optional
from pydantic import BaseModel


class TestResult(BaseModel):
    url: str
    status_code: int
    response_time: float
    success: bool
    reason: Optional[str] = ""
