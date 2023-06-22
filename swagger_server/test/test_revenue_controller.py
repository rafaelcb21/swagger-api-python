# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.revenue import Revenue  # noqa: E501
from swagger_server.models.revenue_response import RevenueResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRevenueController(BaseTestCase):
    """RevenueController integration test stubs"""

    def test_api_vversion_revenues_customer_idpost(self):
        """Test case for api_vversion_revenues_customer_idpost"""
        body = Revenue()
        response = self.client.open(
            "/api/v{version}/revenues/{customerID}".format(
                version="version_example", customer_id=56
            ),
            method="POST",
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_api_vversion_revenues_revenue_iddelete(self):
        """Test case for api_vversion_revenues_revenue_iddelete"""
        response = self.client.open(
            "/api/v{version}/revenues/{revenueID}".format(
                version="version_example", revenue_id=56
            ),
            method="DELETE",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_api_vversion_revenues_revenue_idput(self):
        """Test case for api_vversion_revenues_revenue_idput"""
        body = Revenue()
        response = self.client.open(
            "/api/v{version}/revenues/{revenueID}".format(
                version="version_example", revenue_id=56
            ),
            method="PUT",
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))


if __name__ == "__main__":
    import unittest

    unittest.main()
