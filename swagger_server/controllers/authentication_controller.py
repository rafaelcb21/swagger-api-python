import connexion

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.login import Login  # noqa: E501
from swagger_server.models.login_response import LoginResponse  # noqa: E501
from swagger_server.models.user import User
from swagger_server.models.token import Token  # noqa: E501
from swagger_server import db
from swagger_server.controllers.authorization_controller import check_version

import os
from pathlib import Path
from dotenv import load_dotenv
import jwt


env_path = Path(__file__).resolve().parent.parent.parent / '.env'
load_dotenv(env_path)


def api_vversion_auth_post(version, body=None):  # noqa: E501
    """api_vversion_auth_post

     # noqa: E501

    :param version: Version number
    :type version: str
    :param body: Request to authenticate
    :type body: dict | bytes

    :rtype: LoginResponse
    """

    if check_version(version)['version'] == 'error':
        return Error(error='Unauthorized'), 401

    if connexion.request.is_json:
        body = Login.from_dict(connexion.request.get_json())  # noqa: E501

        session = db.Session()
        user_data = (
            session.query(db.User)
            .filter(
                db.User.email == body.login, db.User.password == body.password
            )
            .first()
        )

        if user_data is not None:
            secret_key = os.environ.get('SECRET_KEY')
            payload = {'sub': body.login}
            token = jwt.encode(payload, secret_key, algorithm='HS256')

            response = LoginResponse(
                token=token,
                user=User(
                    name=user_data.name,
                    email=user_data.email,
                    password=user_data.password,
                    cnpj=user_data.cnpj,
                    company_name=user_data.company_name,
                    phone_number=user_data.phone_number,
                ),
            )
            session.close()
            return response, 201
        return Error(error='Unauthorized'), 401
    return Error(error='Unauthorized'), 401


def api_vversion_users_sso_post(version, body=None):  # noqa: E501
    """api_vversion_users_sso_post

     # noqa: E501

    :param version: Version number
    :type version: str
    :param body: User authentication by SSO
    :type body: dict | bytes

    :rtype: LoginResponse
    """

    if check_version(version)['version'] == 'error':
        return Error(error='Unauthorized'), 401

    if connexion.request.is_json:
        body = Token.from_dict(connexion.request.get_json())  # noqa: E501
        secret_key = os.environ.get('SECRET_KEY')

        try:
            decoded_token = jwt.decode(
                body.app_token, secret_key, algorithms=['HS256']
            )
            if decoded_token['sub'] != body.login:
                return Error(error='Unauthorized'), 401

            session = db.Session()
            user_data = (
                session.query(db.User)
                .filter(db.User.email == body.login)
                .first()
            )

            if user_data is not None:
                response = LoginResponse(
                    token=body.app_token,
                    user=User(
                        name=user_data.name,
                        email=user_data.email,
                        password=user_data.password,
                        cnpj=user_data.cnpj,
                        company_name=user_data.company_name,
                        phone_number=user_data.phone_number,
                    ),
                )
                session.close()
                return response, 201
            return Error(error='Unauthorized'), 401
        except jwt.exceptions.DecodeError:
            return Error(error='Unauthorized'), 401

        except jwt.exceptions.InvalidTokenError:
            return Error(error='Unauthorized'), 401

    return Error(error='Unauthorized'), 401
