# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.fiscal_year import FiscalYear  # noqa: E501
from swagger_server.models.revenue_by_customer import RevenueByCustomer  # noqa: E501
from swagger_server.models.revenue_by_month import RevenueByMonth  # noqa: E501
from swagger_server.models.total_revenue import TotalRevenue  # noqa: E501
from swagger_server.test import BaseTestCase


class TestReportController(BaseTestCase):
    """ReportController integration test stubs"""

    def test_api_vversion_reports_revenue_by_customer_post(self):
        """Test case for api_vversion_reports_revenue_by_customer_post"""
        body = FiscalYear()
        response = self.client.open(
            "/api/v{version}/reports/revenue-by-customer".format(
                version="version_example"
            ),
            method="POST",
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_api_vversion_reports_revenue_by_month_post(self):
        """Test case for api_vversion_reports_revenue_by_month_post"""
        body = FiscalYear()
        response = self.client.open(
            "/api/v{version}/reports/revenue-by-month".format(
                version="version_example"
            ),
            method="POST",
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_api_vversion_reports_total_revenue_post(self):
        """Test case for api_vversion_reports_total_revenue_post"""
        body = FiscalYear()
        response = self.client.open(
            "/api/v{version}/reports/total-revenue".format(version="version_example"),
            method="POST",
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))


if __name__ == "__main__":
    import unittest

    unittest.main()
