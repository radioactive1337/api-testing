import allure

from api.api import Api
from data_models.user_model import UserModel
from data_models.user_list_model import UserListModel


class SendrequestApi(Api):
    _URL = "https://send-request.me"
    _ENDPOINT = "/api/users/"

    @allure.step("creating a user")
    def create_user(self, request_body: UserModel):
        return self.post(url=self._URL,
                         endpoint=self._ENDPOINT,
                         json_body=request_body.model_dump())

    @allure.step("getting a list of users")
    def get_users_list(self, params: UserListModel):
        return self.get(url=self._URL,
                        endpoint=self._ENDPOINT,
                        params=params.model_dump())
