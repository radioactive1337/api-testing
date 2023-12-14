import pytest
import allure

from tools.data_loader import data_loader
from api.send_request_api import SendrequestApi
from data_models.user_model import UserModelResponse


@allure.epic("send-request api")
@allure.feature("Users")
@allure.story("Get One User")
class Test:
    @pytest.mark.parametrize("req_params", data_loader("user_data", "data"))
    @allure.title("request to get a user")
    @pytest.mark.dev
    def test_getting_user(self, req_params, create_user_fixture):
        """
        trying to get info about valid user...
        """
        created_user = create_user_fixture(req_params)
        user_response = SendrequestApi().get_one_user(created_user.get_payload("user_id"))
        user_response.status_code_should_be(200). \
            jsonschema_validation("user_schema"). \
            pydantic_validation(UserModelResponse). \
            check_value_in_response("first_name", created_user.get_payload("first_name")). \
            check_value_in_response("last_name", created_user.get_payload("last_name")). \
            check_value_in_response("company_id", created_user.get_payload("company_id"))

    @pytest.mark.parametrize("req_params", data_loader("user_data", "invalid_user_ids"))
    @allure.title("request to get a user")
    @pytest.mark.dev
    def test_getting_invalid_user(self, req_params):
        """
        trying to get info about invalid user...
        """
        SendrequestApi().get_one_user(req_params). \
            status_code_should_be(404). \
            jsonschema_validation("error_schema")
