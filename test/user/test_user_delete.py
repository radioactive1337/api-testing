import pytest
import allure

from tools.data_loader import data_loader
from api.send_request_api import SendrequestApi
from data_models.error_model import ErrorModelResponse


@allure.epic("send-request api")
@allure.feature("Users")
@allure.story("Delete User")
class Test:
    @pytest.mark.parametrize("req_params", data_loader("user_data", "data"))
    @allure.title("request to delete a user")
    @pytest.mark.dev
    def test_deleting_user(self, req_params, create_user_fixture):
        """
        trying to delete user...
        """
        created_user = create_user_fixture(req_params)
        user_id = created_user.get_payload("user_id")
        delete_user_response = SendrequestApi().delete_user(user_id)
        delete_user_response.status_code_should_be(202)

    @pytest.mark.parametrize("req_params", data_loader("user_data", "invalid_del_user_id"))
    @allure.title("request to delete a user")
    @pytest.mark.dev
    def test_deleting_invalid_user(self, req_params):
        """
        trying to delete user...
        """
        delete_user_response = SendrequestApi().delete_user(uid=req_params)
        delete_user_response.status_code_should_be(404). \
            jsonschema_validation("error_schema"). \
            pydantic_validation(ErrorModelResponse)
