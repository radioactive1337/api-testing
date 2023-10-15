import allure

from api.api import Api
from data_models.create_user_model import CreateUserModelRequest


class SendrequestApi(Api):
    _URL = "https://send-request.me"
    _ENDPOINT = "/api/users/"

    @allure.step("Creating a user")
    def create_user(self, request_body: CreateUserModelRequest):
        return self.post(url=self._URL,
                         endpoint=self._ENDPOINT,
                         json_body=request_body.model_dump())
