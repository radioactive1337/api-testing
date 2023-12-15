import pytest
import allure

from tools.data_loader import data_loader
from api.send_request_api import SendrequestApi
from data_models.user_list_model import UserListModelResponse


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
        get_list_users_response = SendrequestApi().get_users_list(params=req_params)
        get_list_users_response.status_code_should_be(200). \
            jsonschema_validation("users_list_schema"). \
            pydantic_validation(UserListModelResponse)
