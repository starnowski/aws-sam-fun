import os
from unittest import TestCase

import boto3
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
        self.api_endpoint = TestApiGateway.get_stack_name()

    def test_api_gateway(self):
        """
        Call the API Gateway endpoint and check the response
        """
        response = requests.get(self.api_endpoint + "/hello")
        self.assertDictEqual(response.json(), {"message": "hello world"})
