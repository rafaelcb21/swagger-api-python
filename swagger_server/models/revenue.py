# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Revenue(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self,
        amount: float = None,
        invoice_id: str = None,
        description: str = None,
        accrual_date: str = None,
        transaction_date: str = None,
    ):  # noqa: E501
        """Revenue - a model defined in Swagger

        :param amount: The amount of this Revenue.  # noqa: E501
        :type amount: float
        :param invoice_id: The invoice_id of this Revenue.  # noqa: E501
        :type invoice_id: str
        :param description: The description of this Revenue.  # noqa: E501
        :type description: str
        :param accrual_date: The accrual_date of this Revenue.  # noqa: E501
        :type accrual_date: str
        :param transaction_date: The transaction_date of this Revenue.  # noqa: E501
        :type transaction_date: str
        """
        self.swagger_types = {
            'amount': float,
            'invoice_id': str,
            'description': str,
            'accrual_date': str,
            'transaction_date': str,
        }

        self.attribute_map = {
            'amount': 'amount',
            'invoice_id': 'invoice_id',
            'description': 'description',
            'accrual_date': 'accrual_date',
            'transaction_date': 'transaction_date',
        }
        self._amount = amount
        self._invoice_id = invoice_id
        self._description = description
        self._accrual_date = accrual_date
        self._transaction_date = transaction_date

    @classmethod
    def from_dict(cls, dikt) -> 'Revenue':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Revenue of this Revenue.  # noqa: E501
        :rtype: Revenue
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amount(self) -> float:
        """Gets the amount of this Revenue.


        :return: The amount of this Revenue.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount: float):
        """Sets the amount of this Revenue.


        :param amount: The amount of this Revenue.
        :type amount: float
        """

        self._amount = amount

    @property
    def invoice_id(self) -> str:
        """Gets the invoice_id of this Revenue.


        :return: The invoice_id of this Revenue.
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id: str):
        """Sets the invoice_id of this Revenue.


        :param invoice_id: The invoice_id of this Revenue.
        :type invoice_id: str
        """

        self._invoice_id = invoice_id

    @property
    def description(self) -> str:
        """Gets the description of this Revenue.


        :return: The description of this Revenue.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Revenue.


        :param description: The description of this Revenue.
        :type description: str
        """

        self._description = description

    @property
    def accrual_date(self) -> str:
        """Gets the accrual_date of this Revenue.


        :return: The accrual_date of this Revenue.
        :rtype: str
        """
        return self._accrual_date

    @accrual_date.setter
    def accrual_date(self, accrual_date: str):
        """Sets the accrual_date of this Revenue.


        :param accrual_date: The accrual_date of this Revenue.
        :type accrual_date: str
        """

        self._accrual_date = accrual_date

    @property
    def transaction_date(self) -> str:
        """Gets the transaction_date of this Revenue.


        :return: The transaction_date of this Revenue.
        :rtype: str
        """
        return self._transaction_date

    @transaction_date.setter
    def transaction_date(self, transaction_date: str):
        """Sets the transaction_date of this Revenue.


        :param transaction_date: The transaction_date of this Revenue.
        :type transaction_date: str
        """

        self._transaction_date = transaction_date
