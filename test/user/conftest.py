import pytest
from api.send_request_api import SendrequestApi


def _create_user(user_data):
    created_user = SendrequestApi().create_user(req_body=user_data)
    return created_user


@pytest.fixture
def create_user_fixture():
    return _create_user
