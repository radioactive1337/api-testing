import pytest
import allure

from tools.data_loader import data_loader
from api.send_request_api import SendrequestApi
from data.user_data import invalid_data3, invalid_data2, invalid_data1


@allure.epic("send-request api")
@allure.feature("Users")
@allure.story("Create User")
class Test:

    @pytest.mark.parametrize("req_params", data_loader("user_data", "data"))
    @allure.title("request to create a user using valid data\n(params: {req_params})")
    @pytest.mark.dev
    def test_user_creation_valid(self, req_params):
        """
        trying to create a user with valid data...
        """
        SendrequestApi().create_user(req_body=req_params). \
            status_code_should_be(201). \
            jsonschema_should_be_valid("user_schema"). \
            check_value_in_response(["first_name"], req_params.first_name). \
            check_value_in_response(["last_name"], req_params.last_name)

    @pytest.mark.parametrize("req_params", data_loader("user_data", "invalid_data1"))
    @allure.title("request to create a user using invalid data\n(params: {req_params})")
    @pytest.mark.prod
    def test_user_creation_invalid1(self, req_params):
        """
        trying to create a user with invalid data... (status code 422)
        """
        SendrequestApi().create_user(req_body=req_params). \
            status_code_should_be(422). \
            jsonschema_should_be_valid("validation_error_schema")

    @pytest.mark.parametrize("req_params", data_loader("user_data", "invalid_data2"))
    @allure.title("request to create a user using invalid data\n(params: {req_params})")
    @pytest.mark.prod
    def test_user_creation_invalid2(self, req_params):
        """
        trying to create a user with invalid data... (status code 404)
        """
        SendrequestApi().create_user(req_body=req_params). \
            status_code_should_be(404). \
            jsonschema_should_be_valid("error_schema")

    @pytest.mark.parametrize("req_params", data_loader("user_data", "invalid_data3"))
    @allure.title("request to create a user using invalid data\n(params: {req_params})")
    @pytest.mark.prod
    def test_user_creation_invalid3(self, req_params):
        """
        trying to create a user with invalid data... (status code 400)
        """
        SendrequestApi().create_user(req_body=req_params). \
            status_code_should_be(400). \
            jsonschema_should_be_valid("error_schema")

# @allure.title("request to create a user using invalid data")
# @pytest.mark.parametrize("req_params", [invalid_data3, invalid_data2, invalid_data1])
# @pytest.mark.prod
# def test_user_creation_invalid3(self, req_params):
#     """
#     trying to create a user with invalid data... (status code 400,404,422)
#     """
#     SendrequestApi().create_user(req_body=req_params). \
#         status_code_should_be([400, 404, 422]). \
#         jsonschema_should_be_valid("error_schema")
