# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.get_user import GetUser  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_response import UserResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_api_vversion_users_idget(self):
        """Test case for api_vversion_users_idget"""
        response = self.client.open(
            "/api/v{version}/users/{ID}".format(version="version_example", id=56),
            method="GET",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_api_vversion_users_idput(self):
        """Test case for api_vversion_users_idput"""
        body = User()
        response = self.client.open(
            "/api/v{version}/users/{ID}".format(version="version_example", id=56),
            method="PUT",
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_api_vversion_users_post(self):
        """Test case for api_vversion_users_post"""
        body = User()
        response = self.client.open(
            "/api/v{version}/users".format(version="version_example"),
            method="POST",
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))


if __name__ == "__main__":
    import unittest

    unittest.main()
