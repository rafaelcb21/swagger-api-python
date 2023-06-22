# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Category(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self, name: str = None, description: str = None
    ):  # noqa: E501
        """Category - a model defined in Swagger

        :param name: The name of this Category.  # noqa: E501
        :type name: str
        :param description: The description of this Category.  # noqa: E501
        :type description: str
        """
        self.swagger_types = {'name': str, 'description': str}

        self.attribute_map = {'name': 'name', 'description': 'description'}
        self._name = name
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'Category':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Category of this Category.  # noqa: E501
        :rtype: Category
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this Category.


        :return: The name of this Category.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Category.


        :param name: The name of this Category.
        :type name: str
        """

        self._name = name

    @property
    def description(self) -> str:
        """Gets the description of this Category.


        :return: The description of this Category.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Category.


        :param description: The description of this Category.
        :type description: str
        """

        self._description = description
