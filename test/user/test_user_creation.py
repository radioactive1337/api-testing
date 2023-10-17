import pytest
import allure

from tools.data_loader import data_loader
from api.send_request_api import SendrequestApi


@allure.title("request to create a user using valid data")
@pytest.mark.parametrize("req_params", data_loader("user_data", "data"))
def test_user_creation_valid(req_params):
    """
    trying to create a user with valid data...
    """
    SendrequestApi().create_user(request_body=req_params). \
        status_code_should_be(201). \
        jsonschema_should_be_valid("user_creation_response_201"). \
        value_in_response_parameter(["first_name"], req_params.first_name). \
        value_in_response_parameter(["last_name"], req_params.last_name)


@allure.title("request to create a user using invalid data")
@pytest.mark.parametrize("req_params", data_loader("user_data", "invalid_data1"))
def test_user_creation_invalid1(req_params):
    """
    trying to create a user with invalid data... (status code 422)
    """
    SendrequestApi().create_user(request_body=req_params). \
        status_code_should_be(422). \
        jsonschema_should_be_valid("user_creation_response_422")


@allure.title("request to create a user using invalid data")
@pytest.mark.parametrize("req_params", data_loader("user_data", "invalid_data2"))
def test_user_creation_invalid2(req_params):
    """
    trying to create a user with invalid data... (status code 404)
    """
    SendrequestApi().create_user(request_body=req_params). \
        status_code_should_be(404). \
        jsonschema_should_be_valid("user_creation_response_400")


@allure.title("request to create a user using invalid data")
@pytest.mark.parametrize("req_params", data_loader("user_data", "invalid_data3"))
def test_user_creation_invalid3(req_params):
    """
    trying to create a user with invalid data... (status code 400)
    """
    SendrequestApi().create_user(request_body=req_params). \
        status_code_should_be(400). \
        jsonschema_should_be_valid("user_creation_response_400")
