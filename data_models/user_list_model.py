from pydantic import BaseModel, conint
from typing import Any, List, Optional


class UserListModelRequest(BaseModel):
    limit: Any
    offset: Any


class Meta(BaseModel):
    limit: int
    offset: int
    total: int


class Data(BaseModel):
    first_name: Optional[str]
    last_name: str
    company_id: Optional[conint(ge=1, le=3)]
    user_id: conint(gt=0)


class UserListModelResponse(BaseModel):
    meta: Meta
    data: List[Data]
