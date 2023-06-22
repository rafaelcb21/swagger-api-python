# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.setting import Setting  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSettingController(BaseTestCase):
    """SettingController integration test stubs"""

    def test_api_vversion_settings_get(self):
        """Test case for api_vversion_settings_get"""
        response = self.client.open(
            '/api/v{version}/settings'.format(version='version_example'),
            method='GET',
        )
        self.assert200(
            response, 'Response body is : ' + response.data.decode('utf-8')
        )

    def test_api_vversion_settings_put(self):
        """Test case for api_vversion_settings_put"""
        body = Setting()
        response = self.client.open(
            '/api/v{version}/settings'.format(version='version_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
        )
        self.assert200(
            response, 'Response body is : ' + response.data.decode('utf-8')
        )


if __name__ == '__main__':
    import unittest

    unittest.main()
