# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.categories import Categories  # noqa: E501
from swagger_server.models.category import Category  # noqa: E501
from swagger_server.models.category_response import (
    CategoryResponse,
)  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCategoryController(BaseTestCase):
    """CategoryController integration test stubs"""

    def test_api_vversion_categories_category_id_archives_put(self):
        """Test case for api_vversion_categories_category_id_archives_put"""
        response = self.client.open(
            '/api/v{version}/categories/{categoryID}/archives'.format(
                version='version_example', category_id=56
            ),
            method='PUT',
        )
        self.assert200(
            response, 'Response body is : ' + response.data.decode('utf-8')
        )

    def test_api_vversion_categories_category_idget(self):
        """Test case for api_vversion_categories_category_idget"""
        response = self.client.open(
            '/api/v{version}/categories/{categoryID}'.format(
                version='version_example', category_id=56
            ),
            method='GET',
        )
        self.assert200(
            response, 'Response body is : ' + response.data.decode('utf-8')
        )

    def test_api_vversion_categories_category_idput(self):
        """Test case for api_vversion_categories_category_idput"""
        body = Category()
        response = self.client.open(
            '/api/v{version}/categories/{categoryID}'.format(
                version='version_example', category_id=56
            ),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
        )
        self.assert200(
            response, 'Response body is : ' + response.data.decode('utf-8')
        )

    def test_api_vversion_categories_get(self):
        """Test case for api_vversion_categories_get"""
        query_string = [('name', 'name_example')]
        response = self.client.open(
            '/api/v{version}/categories'.format(version='version_example'),
            method='GET',
            query_string=query_string,
        )
        self.assert200(
            response, 'Response body is : ' + response.data.decode('utf-8')
        )

    def test_api_vversion_categories_post(self):
        """Test case for api_vversion_categories_post"""
        body = Category()
        response = self.client.open(
            '/api/v{version}/categories'.format(version='version_example'),
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
