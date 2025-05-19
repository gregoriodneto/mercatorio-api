from pydantic import BaseModel
from typing import Any, Optional

class ResponseModel(BaseModel):
    success: bool
    message: str
    data: Optional[Any] = None