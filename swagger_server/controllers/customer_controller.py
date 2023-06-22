import connexion
import six

from swagger_server.models.customer import Customer  # noqa: E501
from swagger_server.models.customer_response import (
    CustomerResponse,
)  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.get_customer import GetCustomer  # noqa: E501
from swagger_server.models.get_customers import GetCustomers  # noqa: E501
from swagger_server import util
from swagger_server.models.error import Error
from swagger_server.controllers.authorization_controller import (
    check_user_auth,
    check_version,
)


def api_vversion_customers_customer_id_archives_put(
    version, customer_id
):  # noqa: E501
    """api_vversion_customers_customer_id_archives_put

     # noqa: E501

    :param version: Version number
    :type version: str
    :param customer_id: Customer&#x27;s ID
    :type customer_id: int

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


def api_vversion_customers_customer_idget(version, customer_id):  # noqa: E501
    """api_vversion_customers_customer_idget

     # noqa: E501

    :param version: Version number
    :type version: str
    :param customer_id: Customer&#x27;s ID
    :type customer_id: int

    :rtype: GetCustomer
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


def api_vversion_customers_customer_idput(version, customer_id):  # noqa: E501
    """api_vversion_customers_customer_idput

     # noqa: E501

    :param version: Version number
    :type version: str
    :param customer_id: Customer&#x27;s ID
    :type customer_id: int

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


def api_vversion_customers_get(version, name=None, cnpj=None):  # noqa: E501
    """api_vversion_customers_get

     # noqa: E501

    :param version: Version number
    :type version: str
    :param name: Customer&#x27;s name
    :type name: str
    :param cnpj: Customer&#x27;s cnpj
    :type cnpj: str

    :rtype: GetCustomers
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


def api_vversion_customers_post(version, body=None):  # noqa: E501
    """api_vversion_customers_post

     # noqa: E501

    :param version: Version number
    :type version: str
    :param body: Register customer
    :type body: dict | bytes

    :rtype: CustomerResponse
    """
    if check_version(version)['version'] == 'error':
        return Error(error='Unauthorized'), 401

    auth_header = connexion.request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    check = check_user_auth(token)

    if check['test_key'] == 'ok':
        if connexion.request.is_json:
            body = Customer.from_dict(
                connexion.request.get_json()
            )  # noqa: E501
        return 'do some magic!'

    else:
        return Error(error='Unauthorized'), 401
