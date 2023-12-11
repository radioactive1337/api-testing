import pytest
import allure

from tools.data_loader import data_loader
from api.send_request_api import SendrequestApi


@allure.epic("send-request api")
@allure.feature("Users")
@allure.story("Update User")
class Test:
    @pytest.mark.parametrize("req_params, req_body", data_loader("user_data", "update_data"))
    @allure.title("request to update a user")
    def test_updating_user(self, req_params, req_body):
        """
        trying to update user info...
        """
        SendrequestApi().update_user(uid=req_params, req_body=req_body). \
            status_code_should_be(200). \
            jsonschema_validation("user_schema")

    @pytest.mark.parametrize("req_params, req_body", data_loader("user_data", "invalid_update_data"))
    @allure.title("request to update a user")
    def test_updating_user_invalid(self, req_params, req_body):
        """
        trying to update invalid user or invalid info...
        """
        SendrequestApi().update_user(uid=req_params, req_body=req_body). \
            status_code_should_be(404). \
            jsonschema_validation("error_schema")
