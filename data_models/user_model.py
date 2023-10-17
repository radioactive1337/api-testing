from pydantic import BaseModel, conint
from typing import Any


class UserModel(BaseModel):
    first_name: Any
    last_name: Any
    company_id: Any


class UserModelResponse(BaseModel):
    first_name: str
    last_name: str
    company_id: int
    user_id: conint(ge=1, le=3)
