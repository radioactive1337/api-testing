import pytest
import allure

from tools.data_loader import data_loader
from api.send_request_api import SendrequestApi


@allure.title("request to get a user list")
@pytest.mark.parametrize("req_params", data_loader("user_data", "list_data"))
def test_getting_user_list(req_params):
    SendrequestApi().get_users_list(params=req_params). \
        status_code_should_be(200). \
        jsonschema_should_be_valid("users_list_schema")
