from pydantic import BaseModel, conint
from typing import Any, Optional


class UserModel(BaseModel):
    first_name: Any
    last_name: Any
    company_id: Any


class UserModelResponse(BaseModel):
    first_name: Optional[str]
    last_name: str
    company_id: Optional[conint(ge=1, le=3)]
    user_id: int
