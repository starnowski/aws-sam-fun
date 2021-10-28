import os
from unittest import TestCase

import requests

"""
Make sure env variable AWS_SAM_STACK_NAME exists with the name of the stack we are going to test. 
"""


class TestApiGateway(TestCase):
    api_endpoint: str

    @classmethod
    def get_api_endpoint(cls) -> str:
        stack_name = os.environ.get("AWS_SAM_TEST_HOST")
        if not stack_name:
            raise Exception(
                "Cannot find env var AWS_SAM_TEST_HOST. \n"
                "Please setup this environment variable with the local SAM where we are running integration tests."
            )

        return stack_name

    def setUp(self) -> None:
        self.api_endpoint = TestApiGateway.get_api_endpoint()

    def test_api_gateway(self):
        """
        Call the API Gateway endpoint and check the response
        """
        response = requests.get(self.api_endpoint + "/hello")
        self.assertDictEqual(response.json(), {"message": "hello world"})

    def test_api_gateway_get(self):
        """
        Call the API Gateway endpoint and check the response
        """
        response = requests.get(self.api_endpoint + "/someResource")
        self.assertDictEqual(response.json(), {"message": "someResource: get"})

    def test_api_gateway_post(self):
        """
        Call the API Gateway endpoint and check the response
        """
        response = requests.post(self.api_endpoint + "/someResource")
        self.assertDictEqual(response.json(), {"message": "someResource: post"})

    def test_api_gateway_get_with_path_parameter(self):
        """
        Call the API Gateway endpoint and check the response
        """
        response = requests.get(self.api_endpoint + "/someResource/" + "XXX-GGG-ZZZ")
        self.assertDictEqual(response.json(), {"message": "someResource: get with id parameter 'XXX-GGG-ZZZ'"})
