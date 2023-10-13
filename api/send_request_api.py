from api.api import Api
from data_models.create_user_model import CreateUserModelRequest, CreateUserModelResponse


class SendrequestApi(Api):
    _URL = "https://send-request.me"
    _ENDPOINT = "/api/users/"

    def create_user(self, request_body: CreateUserModelRequest):
        return self.post(url=self._URL,
                         endpoint=self._ENDPOINT,
                         json_body=request_body.model_dump())
