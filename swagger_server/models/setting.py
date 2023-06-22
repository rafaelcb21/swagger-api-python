# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Setting(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self,
        max_revenue_amount: float = None,
        sms_notification: bool = None,
        email_notification: bool = None,
    ):  # noqa: E501
        """Setting - a model defined in Swagger

        :param max_revenue_amount: The max_revenue_amount of this Setting.  # noqa: E501
        :type max_revenue_amount: float
        :param sms_notification: The sms_notification of this Setting.  # noqa: E501
        :type sms_notification: bool
        :param email_notification: The email_notification of this Setting.  # noqa: E501
        :type email_notification: bool
        """
        self.swagger_types = {
            "max_revenue_amount": float,
            "sms_notification": bool,
            "email_notification": bool,
        }

        self.attribute_map = {
            "max_revenue_amount": "max_revenue_amount",
            "sms_notification": "sms_notification",
            "email_notification": "email_notification",
        }
        self._max_revenue_amount = max_revenue_amount
        self._sms_notification = sms_notification
        self._email_notification = email_notification

    @classmethod
    def from_dict(cls, dikt) -> "Setting":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Setting of this Setting.  # noqa: E501
        :rtype: Setting
        """
        return util.deserialize_model(dikt, cls)

    @property
    def max_revenue_amount(self) -> float:
        """Gets the max_revenue_amount of this Setting.


        :return: The max_revenue_amount of this Setting.
        :rtype: float
        """
        return self._max_revenue_amount

    @max_revenue_amount.setter
    def max_revenue_amount(self, max_revenue_amount: float):
        """Sets the max_revenue_amount of this Setting.


        :param max_revenue_amount: The max_revenue_amount of this Setting.
        :type max_revenue_amount: float
        """

        self._max_revenue_amount = max_revenue_amount

    @property
    def sms_notification(self) -> bool:
        """Gets the sms_notification of this Setting.


        :return: The sms_notification of this Setting.
        :rtype: bool
        """
        return self._sms_notification

    @sms_notification.setter
    def sms_notification(self, sms_notification: bool):
        """Sets the sms_notification of this Setting.


        :param sms_notification: The sms_notification of this Setting.
        :type sms_notification: bool
        """

        self._sms_notification = sms_notification

    @property
    def email_notification(self) -> bool:
        """Gets the email_notification of this Setting.


        :return: The email_notification of this Setting.
        :rtype: bool
        """
        return self._email_notification

    @email_notification.setter
    def email_notification(self, email_notification: bool):
        """Sets the email_notification of this Setting.


        :param email_notification: The email_notification of this Setting.
        :type email_notification: bool
        """

        self._email_notification = email_notification
