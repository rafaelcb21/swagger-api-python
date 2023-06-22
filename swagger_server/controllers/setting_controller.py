import connexion

from swagger_server import db
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.setting import Setting  # noqa: E501
from swagger_server.models.error import Error
from swagger_server.controllers.authorization_controller import (
    check_user_auth,
    check_version,
)


def api_vversion_settings_get(version):  # noqa: E501
    """api_vversion_settings_get

     # noqa: E501

    :param version: Version number
    :type version: str

    :rtype: Setting
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


def api_vversion_settings_put(version, body=None):  # noqa: E501
    """api_vversion_settings_put

     # noqa: E501

    :param version: Version number
    :type version: str
    :param body: Setting notification
    :type body: dict | bytes

    :rtype: Setting
    """
    if check_version(version)['version'] == 'error':
        return Error(error='Unauthorized'), 401

    auth_header = connexion.request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    check = check_user_auth(token)

    if check['test_key'] == 'ok':
        if connexion.request.is_json:
            body = Setting.from_dict(
                connexion.request.get_json()
            )  # noqa: E501

        return 'do some magic!'

    else:
        return Error(error='Unauthorized'), 401
