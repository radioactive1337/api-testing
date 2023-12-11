import pytest
import allure

from tools.data_loader import data_loader
from api.send_request_api import SendrequestApi


@allure.epic("send-request api")
@allure.feature("Users")
@allure.story("Delete User")
class Test:
    @pytest.mark.parametrize("req_params", data_loader("user_data", "del_user_id"))
    @allure.title("request to delete a user")
    def test_deleting_user(self, req_params):
        """
        trying to delete user...
        """
        SendrequestApi().delete_user(uid=req_params). \
            status_code_should_be(202)

    @pytest.mark.parametrize("req_params", data_loader("user_data", "invalid_del_user_id"))
    @allure.title("request to delete a user")
    def test_deleting_invalid_user(self, req_params):
        """
        trying to delete user...
        """
        SendrequestApi().delete_user(uid=req_params). \
            status_code_should_be(404). \
            jsonschema_validation("error_schema")
