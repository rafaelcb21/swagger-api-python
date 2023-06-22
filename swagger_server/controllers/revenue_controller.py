import connexion

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.revenue import Revenue  # noqa: E501
from swagger_server.models.revenue_response import (
    RevenueResponse,
)  # noqa: E501
from swagger_server import util
from swagger_server.models.error import Error
from swagger_server.controllers.authorization_controller import (
    check_user_auth,
    check_version,
)


def api_vversion_revenues_customer_idpost(
    version, customer_id, body=None
):  # noqa: E501
    """api_vversion_revenues_customer_idpost

     # noqa: E501

    :param version: Version number
    :type version: str
    :param customer_id: Customer&#x27;s ID
    :type customer_id: int
    :param body: Register revenue
    :type body: dict | bytes

    :rtype: RevenueResponse
    """
    if check_version(version)['version'] == 'error':
        return Error(error='Unauthorized'), 401

    auth_header = connexion.request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    check = check_user_auth(token)

    if check['test_key'] == 'ok':
        if connexion.request.is_json:
            body = Revenue.from_dict(
                connexion.request.get_json()
            )  # noqa: E501
        return 'do some magic!'

    else:
        return Error(error='Unauthorized'), 401


def api_vversion_revenues_revenue_iddelete(version, revenue_id):  # noqa: E501
    """api_vversion_revenues_revenue_iddelete

     # noqa: E501

    :param version: Version number
    :type version: str
    :param revenue_id: Revenue&#x27;s ID
    :type revenue_id: int

    :rtype: None
    """
    if check_version(version)['version'] == 'error':
        return Error(error='Unauthorized'), 401

    auth_header = connexion.request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    check = check_user_auth(token)

    if check['test_key'] == 'ok':
        return 'do some magic!'

    else:
        return Error(error='Unauthorized'), 401


def api_vversion_revenues_revenue_idput(
    version, revenue_id, body=None
):  # noqa: E501
    """api_vversion_revenues_revenue_idput

     # noqa: E501

    :param version: Version number
    :type version: str
    :param revenue_id: Revenue&#x27;s ID
    :type revenue_id: int
    :param body: Update revenue
    :type body: dict | bytes

    :rtype: None
    """
    if check_version(version)['version'] == 'error':
        return Error(error='Unauthorized'), 401

    auth_header = connexion.request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    check = check_user_auth(token)

    if check['test_key'] == 'ok':
        if connexion.request.is_json:
            body = Revenue.from_dict(
                connexion.request.get_json()
            )  # noqa: E501
        return 'do some magic!'

    else:
        return Error(error='Unauthorized'), 401
