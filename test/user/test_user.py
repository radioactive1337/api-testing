import pytest
import allure

from tools.data_loader import data_loader
from api.send_request_api import SendrequestApi


@allure.epic("send-request api")
@allure.feature("Users")
@allure.story("Get One User")
class Test:
    @pytest.mark.parametrize("req_params", data_loader("user_data", "user_ids"))
    @allure.title("request to get a user")
    def test_getting_user(self, req_params):
        """
        trying to get info about valid user...
        """
        SendrequestApi().get_one_user(req_params). \
            status_code_should_be(200). \
            jsonschema_should_be_valid("user_schema")

    @pytest.mark.parametrize("req_params", data_loader("user_data", "invalid_user_ids"))
    @allure.title("request to get a user")
    def test_getting_invalid_user(self, req_params):
        """
        trying to get info about invalid user...
        """
        SendrequestApi().get_one_user(req_params). \
            status_code_should_be(404). \
            jsonschema_should_be_valid("error_schema")
