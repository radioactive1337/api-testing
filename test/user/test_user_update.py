import pytest
import allure

from tools.data_loader import data_loader
from api.send_request_api import SendrequestApi
from data_models.user_model import UserModelResponse
from data_models.error_model import ErrorModelResponse


@allure.epic("send-request api")
@allure.feature("Users")
@allure.story("Update User")
class Test:
    @pytest.mark.parametrize("user_data, req_body", data_loader("user_data", "update_data"))
    @allure.title("request to update a user")
    @pytest.mark.dev
    def test_updating_user(self, req_body, create_user_fixture, user_data):
        """
        trying to update user info...
        """
        created_user = create_user_fixture(user_data)
        user_id = created_user.get_payload("user_id")
        update_user_response = SendrequestApi().update_user(uid=user_id, req_body=req_body)
        update_user_response.status_code_should_be(200). \
            jsonschema_validation("user_schema"). \
            pydantic_validation(UserModelResponse)

    @pytest.mark.parametrize("user_data, req_body", data_loader("user_data", "invalid_update_data"))
    @allure.title("request to update a user")
    @pytest.mark.dev
    def test_updating_user_invalid(self, req_body, create_user_fixture, user_data):
        """
        trying to update invalid user or invalid info...
        """
        created_user = create_user_fixture(user_data)
        user_id = created_user.get_payload("user_id")
        update_user_response = SendrequestApi().update_user(uid=user_id, req_body=req_body)
        update_user_response.status_code_should_be([422, 404]). \
            jsonschema_validation("error_schema"). \
            pydantic_validation(ErrorModelResponse)

    @pytest.mark.parametrize("user_id, req_body", data_loader("user_data", "invalid_update_data2"))
    @allure.title("request to update a user")
    @pytest.mark.dev
    def test_updating_user_invalid(self, req_body, user_id):
        """
        trying to update invalid user or invalid user id...
        """
        update_user_response = SendrequestApi().update_user(uid=user_id, req_body=req_body)
        update_user_response.status_code_should_be([422, 404]). \
            jsonschema_validation("error_schema"). \
            pydantic_validation(ErrorModelResponse)
