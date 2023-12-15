from pydantic import BaseModel
from typing import List


class Detail1(BaseModel):
    loc: List[str | int]
    msg: str
    type: str


class Detail2(BaseModel):
    reason: str


class ErrorModelResponse(BaseModel):
    detail: List[Detail1] | Detail2
