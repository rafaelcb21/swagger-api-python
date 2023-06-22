# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.expense import Expense  # noqa: E501
from swagger_server.models.expense_response import (
    ExpenseResponse,
)  # noqa: E501
from swagger_server.test import BaseTestCase


class TestExpenseController(BaseTestCase):
    """ExpenseController integration test stubs"""

    def test_api_vversion_expenses_category_idpost(self):
        """Test case for api_vversion_expenses_category_idpost"""
        body = Expense()
        response = self.client.open(
            '/api/v{version}/expenses/{categoryID}'.format(
                version='version_example', category_id=56
            ),
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
        )
        self.assert200(
            response, 'Response body is : ' + response.data.decode('utf-8')
        )

    def test_api_vversion_expenses_expense_iddelete(self):
        """Test case for api_vversion_expenses_expense_iddelete"""
        response = self.client.open(
            '/api/v{version}/expenses/{expenseID}'.format(
                version='version_example', expense_id=56
            ),
            method='DELETE',
        )
        self.assert200(
            response, 'Response body is : ' + response.data.decode('utf-8')
        )

    def test_api_vversion_expenses_expense_idput(self):
        """Test case for api_vversion_expenses_expense_idput"""
        body = Expense()
        response = self.client.open(
            '/api/v{version}/expenses/{expenseID}'.format(
                version='version_example', expense_id=56
            ),
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
