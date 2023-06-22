# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.category import Category  # noqa: F401,E501
from swagger_server import util


class Categories(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self, count: int = None, categories: List[Category] = None
    ):  # noqa: E501
        """Categories - a model defined in Swagger

        :param count: The count of this Categories.  # noqa: E501
        :type count: int
        :param categories: The categories of this Categories.  # noqa: E501
        :type categories: List[Category]
        """
        self.swagger_types = {"count": int, "categories": List[Category]}

        self.attribute_map = {"count": "count", "categories": "categories"}
        self._count = count
        self._categories = categories

    @classmethod
    def from_dict(cls, dikt) -> "Categories":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Categories of this Categories.  # noqa: E501
        :rtype: Categories
        """
        return util.deserialize_model(dikt, cls)

    @property
    def count(self) -> int:
        """Gets the count of this Categories.


        :return: The count of this Categories.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count: int):
        """Sets the count of this Categories.


        :param count: The count of this Categories.
        :type count: int
        """

        self._count = count

    @property
    def categories(self) -> List[Category]:
        """Gets the categories of this Categories.


        :return: The categories of this Categories.
        :rtype: List[Category]
        """
        return self._categories

    @categories.setter
    def categories(self, categories: List[Category]):
        """Sets the categories of this Categories.


        :param categories: The categories of this Categories.
        :type categories: List[Category]
        """

        self._categories = categories
