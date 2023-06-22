# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RevenueResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, revenue_id: int = None):  # noqa: E501
        """RevenueResponse - a model defined in Swagger

        :param revenue_id: The revenue_id of this RevenueResponse.  # noqa: E501
        :type revenue_id: int
        """
        self.swagger_types = {"revenue_id": int}

        self.attribute_map = {"revenue_id": "revenue_id"}
        self._revenue_id = revenue_id

    @classmethod
    def from_dict(cls, dikt) -> "RevenueResponse":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RevenueResponse of this RevenueResponse.  # noqa: E501
        :rtype: RevenueResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def revenue_id(self) -> int:
        """Gets the revenue_id of this RevenueResponse.


        :return: The revenue_id of this RevenueResponse.
        :rtype: int
        """
        return self._revenue_id

    @revenue_id.setter
    def revenue_id(self, revenue_id: int):
        """Sets the revenue_id of this RevenueResponse.


        :param revenue_id: The revenue_id of this RevenueResponse.
        :type revenue_id: int
        """

        self._revenue_id = revenue_id
