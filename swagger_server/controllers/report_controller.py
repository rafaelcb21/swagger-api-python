import connexion

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.fiscal_year import FiscalYear  # noqa: E501
from swagger_server.models.revenue_by_customer import (
    RevenueByCustomer,
)  # noqa: E501
from swagger_server.models.revenue_by_month import RevenueByMonth  # noqa: E501
from swagger_server.models.total_revenue import TotalRevenue  # noqa: E501
from swagger_server import util
from swagger_server.models.error import Error
from swagger_server.controllers.authorization_controller import (
    check_user_auth,
    check_version,
)


def api_vversion_reports_revenue_by_customer_post(
    version, body=None
):  # noqa: E501
    """api_vversion_reports_revenue_by_customer_post

     # noqa: E501

    :param version: Version number
    :type version: str
    :param body: Fiscal Year
    :type body: dict | bytes

    :rtype: RevenueByCustomer
    """
    if check_version(version)['version'] == 'error':
        return Error(error='Unauthorized'), 401

    auth_header = connexion.request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    check = check_user_auth(token)

    if check['test_key'] == 'ok':
        if connexion.request.is_json:
            body = FiscalYear.from_dict(
                connexion.request.get_json()
            )  # noqa: E501
        return 'do some magic!'

    else:
        return Error(error='Unauthorized'), 401


def api_vversion_reports_revenue_by_month_post(
    version, body=None
):  # noqa: E501
    """api_vversion_reports_revenue_by_month_post

     # noqa: E501

    :param version: Version number
    :type version: str
    :param body: Fiscal Year
    :type body: dict | bytes

    :rtype: RevenueByMonth
    """
    if check_version(version)['version'] == 'error':
        return Error(error='Unauthorized'), 401

    auth_header = connexion.request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    check = check_user_auth(token)

    if check['test_key'] == 'ok':
        if connexion.request.is_json:
            body = FiscalYear.from_dict(
                connexion.request.get_json()
            )  # noqa: E501
        return 'do some magic!'

    else:
        return Error(error='Unauthorized'), 401


def api_vversion_reports_total_revenue_post(version, body=None):  # noqa: E501
    """api_vversion_reports_total_revenue_post

     # noqa: E501

    :param version: Version number
    :type version: str
    :param body: Register customer
    :type body: dict | bytes

    :rtype: TotalRevenue
    """
    if check_version(version)['version'] == 'error':
        return Error(error='Unauthorized'), 401

    auth_header = connexion.request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    check = check_user_auth(token)

    if check['test_key'] == 'ok':
        if connexion.request.is_json:
            body = FiscalYear.from_dict(
                connexion.request.get_json()
            )  # noqa: E501
        return 'do some magic!'

    else:
        return Error(error='Unauthorized'), 401
