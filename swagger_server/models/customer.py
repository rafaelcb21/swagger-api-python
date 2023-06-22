# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Customer(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self,
        cnpj: str = None,
        commercial_name: str = None,
        legal_name: str = None,
    ):  # noqa: E501
        """Customer - a model defined in Swagger

        :param cnpj: The cnpj of this Customer.  # noqa: E501
        :type cnpj: str
        :param commercial_name: The commercial_name of this Customer.  # noqa: E501
        :type commercial_name: str
        :param legal_name: The legal_name of this Customer.  # noqa: E501
        :type legal_name: str
        """
        self.swagger_types = {
            'cnpj': str,
            'commercial_name': str,
            'legal_name': str,
        }

        self.attribute_map = {
            'cnpj': 'cnpj',
            'commercial_name': 'commercial_name',
            'legal_name': 'legal_name',
        }
        self._cnpj = cnpj
        self._commercial_name = commercial_name
        self._legal_name = legal_name

    @classmethod
    def from_dict(cls, dikt) -> 'Customer':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Customer of this Customer.  # noqa: E501
        :rtype: Customer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cnpj(self) -> str:
        """Gets the cnpj of this Customer.


        :return: The cnpj of this Customer.
        :rtype: str
        """
        return self._cnpj

    @cnpj.setter
    def cnpj(self, cnpj: str):
        """Sets the cnpj of this Customer.


        :param cnpj: The cnpj of this Customer.
        :type cnpj: str
        """

        self._cnpj = cnpj

    @property
    def commercial_name(self) -> str:
        """Gets the commercial_name of this Customer.


        :return: The commercial_name of this Customer.
        :rtype: str
        """
        return self._commercial_name

    @commercial_name.setter
    def commercial_name(self, commercial_name: str):
        """Sets the commercial_name of this Customer.


        :param commercial_name: The commercial_name of this Customer.
        :type commercial_name: str
        """

        self._commercial_name = commercial_name

    @property
    def legal_name(self) -> str:
        """Gets the legal_name of this Customer.


        :return: The legal_name of this Customer.
        :rtype: str
        """
        return self._legal_name

    @legal_name.setter
    def legal_name(self, legal_name: str):
        """Sets the legal_name of this Customer.


        :param legal_name: The legal_name of this Customer.
        :type legal_name: str
        """

        self._legal_name = legal_name
