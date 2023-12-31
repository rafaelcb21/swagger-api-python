# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.month_revenue import MonthRevenue  # noqa: F401,E501
from swagger_server import util


class RevenueByMonth(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self,
        max_revenue_amount: float = None,
        revenue: List[MonthRevenue] = None,
    ):  # noqa: E501
        """RevenueByMonth - a model defined in Swagger

        :param max_revenue_amount: The max_revenue_amount of this RevenueByMonth.  # noqa: E501
        :type max_revenue_amount: float
        :param revenue: The revenue of this RevenueByMonth.  # noqa: E501
        :type revenue: List[MonthRevenue]
        """
        self.swagger_types = {
            'max_revenue_amount': float,
            'revenue': List[MonthRevenue],
        }

        self.attribute_map = {
            'max_revenue_amount': 'max_revenue_amount',
            'revenue': 'revenue',
        }
        self._max_revenue_amount = max_revenue_amount
        self._revenue = revenue

    @classmethod
    def from_dict(cls, dikt) -> 'RevenueByMonth':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RevenueByMonth of this RevenueByMonth.  # noqa: E501
        :rtype: RevenueByMonth
        """
        return util.deserialize_model(dikt, cls)

    @property
    def max_revenue_amount(self) -> float:
        """Gets the max_revenue_amount of this RevenueByMonth.


        :return: The max_revenue_amount of this RevenueByMonth.
        :rtype: float
        """
        return self._max_revenue_amount

    @max_revenue_amount.setter
    def max_revenue_amount(self, max_revenue_amount: float):
        """Sets the max_revenue_amount of this RevenueByMonth.


        :param max_revenue_amount: The max_revenue_amount of this RevenueByMonth.
        :type max_revenue_amount: float
        """

        self._max_revenue_amount = max_revenue_amount

    @property
    def revenue(self) -> List[MonthRevenue]:
        """Gets the revenue of this RevenueByMonth.


        :return: The revenue of this RevenueByMonth.
        :rtype: List[MonthRevenue]
        """
        return self._revenue

    @revenue.setter
    def revenue(self, revenue: List[MonthRevenue]):
        """Sets the revenue of this RevenueByMonth.


        :param revenue: The revenue of this RevenueByMonth.
        :type revenue: List[MonthRevenue]
        """

        self._revenue = revenue
