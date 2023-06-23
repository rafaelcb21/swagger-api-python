import connexion

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.get_user import GetUser  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import db
from swagger_server.controllers.authorization_controller import (
    check_user_auth,
    check_version,
)
from swagger_server.models.user_response import UserResponse


def api_vversion_users_idget(version, id_):  # noqa: E501
    """api_vversion_users_idget

     # noqa: E501

    :param version: Version number
    :type version: str
    :param id: User s ID
    :type id: int

    :rtype: GetUser
    """

    if check_version(version)['version'] == 'error':
        return Error(error='Unauthorized'), 401

    auth_header = connexion.request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    check = check_user_auth(token)

    if check['test_key'] == 'ok':
        session = db.Session()
        user_data = session.query(db.User).get(id_)

        if user_data is None:
            return Error(error='Not Found'), 404

        response = GetUser(
            user=User(
                name=user_data.name,
                email=user_data.email,
                password=user_data.password,
                cnpj=user_data.cnpj,
                company_name=user_data.company_name,
                phone_number=user_data.phone_number,
            )
        )

        session.close()

        return response, 200

    else:
        return Error(error='Unauthorized'), 401


def api_vversion_users_idput(version, id_, body=None):  # noqa: E501
    """api_vversion_users_idput

     # noqa: E501

    :param version: Version number
    :type version: str
    :param id: User s ID
    :type id: int
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
            body = User.from_dict(connexion.request.get_json())  # noqa: E501

            session = db.Session()
            user_data = session.query(db.User).get(id_)

            if user_data is None:
                return Error(error='Not Found'), 404

            user_data.cnpj = body.cnpj
            user_data.company_name = body.company_name
            user_data.email = body.email
            user_data.name = body.name
            user_data.password = body.password
            user_data.phone_number = body.phone_number

            session.commit()
            session.close()
    else:
        return Error(error='Unauthorized'), 401


def api_vversion_users_post(version, body=None):  # noqa: E501
    """api_vversion_users_post

     # noqa: E501

    :param version: Version number
    :type version: str
    :param body: Register user
    :type body: dict | bytes

    :rtype: UserResponse
    """
    if check_version(version)['version'] == 'error':
        return Error(error='Unauthorized'), 401

    auth_header = connexion.request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    check = check_user_auth(token)

    if check['test_key'] == 'ok':
        if connexion.request.is_json:
            body = User.from_dict(connexion.request.get_json())  # noqa: E501

            session = db.Session()
            register = db.User(
                cnpj=body.cnpj,
                company_name=body.company_name,
                email=body.email,
                name=body.name,
                password=body.password,
                phone_number=body.phone_number,
            )
            session.add(register)
            session.commit()

            response = UserResponse(user_id=register.id)

            session.close()

            return response, 201

        return Error(error='Unauthorized'), 401

    else:
        return Error(error='Unauthorized'), 401
