import pytest
import allure

from data_models.create_user_model import CreateUserModelRequest
from tools.data_loader import data_loader
from api.send_request_api import SendrequestApi


@allure.title("Creating a user")
@pytest.mark.parametrize("req_params", data_loader("user_data", "data"))
def test_user_creation(req_params):
    """
    trying to create a user ...
    """
    SendrequestApi().create_user(
        request_body=req_params). \
        status_code_should_be(201). \
        jsonschema_should_be_valid("one_user_schema"). \
        value_in_response_parameter(["first_name"], req_params.first_name). \
        value_in_response_parameter(["last_name"], req_params.last_name)
