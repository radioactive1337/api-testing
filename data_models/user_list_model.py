from pydantic import BaseModel, conint


class UserListModel(BaseModel):
    limit: int | None
    offset: int | None

