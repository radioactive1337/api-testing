import pytest
import allure

from tools.data_loader import data_loader
from api.send_request_api import SendrequestApi


@allure.epic("send-request api")
@allure.feature("Users")
@allure.story("Get Users List")
class Test:
    @pytest.mark.parametrize("req_params", data_loader("user_data", "list_data"))
    @allure.title("request to get a users list")
    def test_getting_user_list(self, req_params):
        """
        trying to get a list of users...
        """
        SendrequestApi().get_users_list(params=req_params). \
            status_code_should_be(200). \
            jsonschema_should_be_valid("users_list_schema")
