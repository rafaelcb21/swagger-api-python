# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CustomerRevenue(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self, customer_name: str = None, revenue: float = None
    ):  # noqa: E501
        """CustomerRevenue - a model defined in Swagger

        :param customer_name: The customer_name of this CustomerRevenue.  # noqa: E501
        :type customer_name: str
        :param revenue: The revenue of this CustomerRevenue.  # noqa: E501
        :type revenue: float
        """
        self.swagger_types = {'customer_name': str, 'revenue': float}

        self.attribute_map = {
            'customer_name': 'customer_name',
            'revenue': 'revenue',
        }
        self._customer_name = customer_name
        self._revenue = revenue

    @classmethod
    def from_dict(cls, dikt) -> 'CustomerRevenue':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CustomerRevenue of this CustomerRevenue.  # noqa: E501
        :rtype: CustomerRevenue
        """
        return util.deserialize_model(dikt, cls)

    @property
    def customer_name(self) -> str:
        """Gets the customer_name of this CustomerRevenue.


        :return: The customer_name of this CustomerRevenue.
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name: str):
        """Sets the customer_name of this CustomerRevenue.


        :param customer_name: The customer_name of this CustomerRevenue.
        :type customer_name: str
        """

        self._customer_name = customer_name

    @property
    def revenue(self) -> float:
        """Gets the revenue of this CustomerRevenue.


        :return: The revenue of this CustomerRevenue.
        :rtype: float
        """
        return self._revenue

    @revenue.setter
    def revenue(self, revenue: float):
        """Sets the revenue of this CustomerRevenue.


        :param revenue: The revenue of this CustomerRevenue.
        :type revenue: float
        """

        self._revenue = revenue
