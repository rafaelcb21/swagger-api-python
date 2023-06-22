# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Token(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, login: str = None, app_token: str = None):  # noqa: E501
        """Token - a model defined in Swagger

        :param login: The login of this Token.  # noqa: E501
        :type login: str
        :param app_token: The app_token of this Token.  # noqa: E501
        :type app_token: str
        """
        self.swagger_types = {"login": str, "app_token": str}

        self.attribute_map = {"login": "login", "app_token": "app_token"}
        self._login = login
        self._app_token = app_token

    @classmethod
    def from_dict(cls, dikt) -> "Token":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Token of this Token.  # noqa: E501
        :rtype: Token
        """
        return util.deserialize_model(dikt, cls)

    @property
    def login(self) -> str:
        """Gets the login of this Token.


        :return: The login of this Token.
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login: str):
        """Sets the login of this Token.


        :param login: The login of this Token.
        :type login: str
        """

        self._login = login

    @property
    def app_token(self) -> str:
        """Gets the app_token of this Token.


        :return: The app_token of this Token.
        :rtype: str
        """
        return self._app_token

    @app_token.setter
    def app_token(self, app_token: str):
        """Sets the app_token of this Token.


        :param app_token: The app_token of this Token.
        :type app_token: str
        """

        self._app_token = app_token
