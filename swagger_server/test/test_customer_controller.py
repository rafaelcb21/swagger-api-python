# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.customer import Customer  # noqa: E501
from swagger_server.models.customer_response import (
    CustomerResponse,
)  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.get_customer import GetCustomer  # noqa: E501
from swagger_server.models.get_customers import GetCustomers  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCustomerController(BaseTestCase):
    """CustomerController integration test stubs"""

    def test_api_vversion_customers_customer_id_archives_put(self):
        """Test case for api_vversion_customers_customer_id_archives_put"""
        response = self.client.open(
            '/api/v{version}/customers/{customerID}/archives'.format(
                version='version_example', customer_id=56
            ),
            method='PUT',
        )
        self.assert200(
            response, 'Response body is : ' + response.data.decode('utf-8')
        )

    def test_api_vversion_customers_customer_idget(self):
        """Test case for api_vversion_customers_customer_idget"""
        response = self.client.open(
            '/api/v{version}/customers/{customerID}'.format(
                version='version_example', customer_id=56
            ),
            method='GET',
        )
        self.assert200(
            response, 'Response body is : ' + response.data.decode('utf-8')
        )

    def test_api_vversion_customers_customer_idput(self):
        """Test case for api_vversion_customers_customer_idput"""
        response = self.client.open(
            '/api/v{version}/customers/{customerID}'.format(
                version='version_example', customer_id=56
            ),
            method='PUT',
        )
        self.assert200(
            response, 'Response body is : ' + response.data.decode('utf-8')
        )

    def test_api_vversion_customers_get(self):
        """Test case for api_vversion_customers_get"""
        query_string = [('name', 'name_example'), ('cnpj', 'cnpj_example')]
        response = self.client.open(
            '/api/v{version}/customers'.format(version='version_example'),
            method='GET',
            query_string=query_string,
        )
        self.assert200(
            response, 'Response body is : ' + response.data.decode('utf-8')
        )

    def test_api_vversion_customers_post(self):
        """Test case for api_vversion_customers_post"""
        body = Customer()
        response = self.client.open(
            '/api/v{version}/customers'.format(version='version_example'),
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
