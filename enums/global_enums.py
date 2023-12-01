from enum import Enum


class ErrorEnums(Enum):
    WRONG_STATUS_CODE = "Received status code is not equal to expected"
    ITEM_DOES_NOT_EXIST = "There are no such items in the response"
