from pydantic import BaseModel, conint


class CreateUserModelRequest(BaseModel):
    first_name: str
    last_name: str
    company_id: int


class CreateUserModelResponse(BaseModel):
    first_name: str
    last_name: str
    company_id: int
    user_id: conint(ge=1, le=3)
