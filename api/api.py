import requests
import allure
from jsonschema import validate
from tools.logger import log
from tools.data_loader import jsonschema_loader
from tools.json_parser import get_data


class Api:

    def __init__(self):
        self.response = None

    def get(self, url: str, endpoint: str, params: dict = None):
        with allure.step(f"POST request на url: {url}{endpoint}\n"):
            self.response = requests.get(url=f"{url}{endpoint}",
                                         params=params)
        log(response=self.response)
        return self

    def post(self, url: str, endpoint: str, params: dict = None,
             json_body: dict = None):
        with allure.step(f"POST request на url: {url}{endpoint}\n"
                         f"request body: {json_body}"):
            self.response = requests.post(url=f"{url}{endpoint}",
                                          params=params,
                                          json=json_body)
        log(response=self.response, request_body=json_body)
        return self

    def put(self, url: str, endpoint: str, params: dict = None, json_body: dict = None):
        with allure.step(f"PUT request на url: {url}{endpoint}\n"
                         f"request body: {json_body}"):
            self.response = requests.put(url=f"{url}{endpoint}",
                                         params=params,
                                         json=json_body)
        log(response=self.response, request_body=json_body)
        return self

    def patch(self, url: str, endpoint: str, params: dict = None, json_body: dict = None):
        with allure.step(f"PATCH request на url: {url}{endpoint}\n"
                         f"request body: {json_body}"):
            self.response = requests.patch(url=f"{url}{endpoint}",
                                           params=params,
                                           json=json_body)
        log(response=self.response, request_body=json_body)
        return self

    def delete(self, url: str, endpoint: str):
        with allure.step(f"DELETE request на url: {url}{endpoint}\n"):
            self.response = requests.delete(url=f"{url}{endpoint}")
        log(response=self.response)
        return self

    @allure.step("status code is equal to {expected_code}")
    def status_code_should_be(self, expected_code):
        actual_code = self.response.status_code
        assert actual_code == expected_code, f"Expected result:{expected_code}\nActual result:{actual_code}"
        return self

    @allure.step("jsonschema is valid")
    def jsonschema_should_be_valid(self, path_file: str, name_jsonschema: str = 'schema'):
        json_schema = jsonschema_loader(path_file, name_jsonschema)
        validate(self.response.json(), json_schema)
        return self

    def get_payload(self, keys: list):
        response = self.response.json()
        payload = get_data(keys, response)
        return payload

    @allure.step("there is a desired value in the response")
    def value_in_response_parameter(self, keys: list, value: str):
        payload = self.get_payload(keys)
        assert (value == payload), f"Expected result:{value}\nActual result:{payload}"
        return self
