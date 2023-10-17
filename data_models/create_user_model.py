from pydantic import BaseModel, conint
from typing import Any


class CreateUserModelRequest(BaseModel):
    first_name: Any
    last_name: Any
    company_id: Any

    def to_dict(self):
        return self.model_dump()


class CreateUserModelResponse(BaseModel):
    first_name: str
    last_name: str
    company_id: int
    user_id: conint(ge=1, le=3)
