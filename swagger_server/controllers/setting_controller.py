import connexion

from swagger_server import db
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.setting import Setting  # noqa: E501
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
        session = db.Session()

        user_data = session.query(db.Setting).first()

        if user_data is None:
            return Error(error='Not Found'), 404

        response = Setting(
            email_notification=user_data.email_notification,
            max_revenue_amount=user_data.max_revenue_amount,
            sms_notification=user_data.sms_notification,
        )

        session.close()

        return response, 200
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

            session = db.Session()

            user_data = session.query(db.Setting).first()

            if user_data is None:
                register = db.Setting(
                    email_notification=body.email_notification,
                    max_revenue_amount=body.max_revenue_amount,
                    sms_notification=body.sms_notification,
                )
                session.add(register)

            else:
                user_data.email_notification = body.email_notification
                user_data.max_revenue_amount = body.max_revenue_amount
                user_data.sms_notification = body.sms_notification

            session.commit()
            session.close()
    else:
        return Error(error='Unauthorized'), 401
