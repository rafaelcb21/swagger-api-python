# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.login import Login  # noqa: E501
from swagger_server.models.login_response import LoginResponse  # noqa: E501
from swagger_server.models.token import Token  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAuthenticationController(BaseTestCase):
    """AuthenticationController integration test stubs"""

    def test_api_vversion_auth_post(self):
        """Test case for api_vversion_auth_post"""
        body = Login()
        response = self.client.open(
            '/api/v{version}/auth'.format(version='version_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
        )
        self.assert200(
            response, 'Response body is : ' + response.data.decode('utf-8')
        )

    def test_api_vversion_users_sso_post(self):
        """Test case for api_vversion_users_sso_post"""
        body = Token()
        response = self.client.open(
            '/api/v{version}/users/sso'.format(version='version_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
        )
        self.assert200(
            response, 'Response body is : ' + response.data.decode('utf-8')
        )


if __name__ == '__main__':
    import unittest

    unittest.main()
