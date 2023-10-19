import allure

from api.api import Api
from data_models.user_model import UserModel
from data_models.user_list_model import UserListModel


class SendrequestApi(Api):
    _URL = "https://send-request.me"
    _ENDPOINT = "/api/users/"

    def create_user(self, req_body: UserModel):
        with allure.step("creating a user"):
            return self.post(url=self._URL,
                             endpoint=self._ENDPOINT,
                             json_body=req_body.model_dump())

    def get_users_list(self, params: UserListModel):
        with allure.step("getting a list of users"):
            return self.get(url=self._URL,
                            endpoint=self._ENDPOINT,
                            params=params.model_dump())

    def get_one_user(self, uid: int):
        with allure.step("getting user"):
            return self.get(url=self._URL,
                            endpoint=self._ENDPOINT + f"{uid}")

    def update_user(self, uid: int, req_body: UserModel):
        with allure.step("updating user"):
            return self.put(url=self._URL,
                            endpoint=self._ENDPOINT + f"{uid}",
                            json_body=req_body.model_dump())

    def delete_user(self, uid: int):
        with allure.step("deleting user"):
            return self.delete(url=self._URL,
                               endpoint=self._ENDPOINT + f"{uid}")
