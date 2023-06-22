import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.get_user import GetUser  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.get_user import GetUser  # noqa: E501
from swagger_server import util, db
from swagger_server.controllers.authorization_controller import (
    check_user_auth,
    check_version,
)
from swagger_server.models.error import Error
from swagger_server.models.user_response import UserResponse


def api_vversion_users_idget(version, id_):  # noqa: E501
    """api_vversion_users_idget

     # noqa: E501

    :param version: Version number
    :type version: str
    :param id: User&#x27;s ID
    :type id: int

    :rtype: GetUser
    """

    if check_version(version)["version"] == "error":
        return Error(error="Unauthorized"), 401

    auth_header = connexion.request.headers.get("Authorization")
    token = auth_header.split(" ")[1]
    check = check_user_auth(token)

    if check["test_key"] == "ok":
        session = db.Session()
        user_data = session.query(db.User).filter(db.User.id == id_).all()

        if len(user_data) > 0:
            for field in user_data:
                response = GetUser(
                    user=User(
                        name=field.name,
                        email=field.email,
                        password=field.password,
                        cnpj=field.cnpj,
                        company_name=field.company_name,
                        phone_number=field.phone_number,
                    )
                )
            session.close()
            return response, 201
        return Error(error="Not Found"), 404

    else:
        return Error(error="Unauthorized"), 401


def api_vversion_users_idput(version, id_, body=None):  # noqa: E501
    """api_vversion_users_idput

     # noqa: E501

    :param version: Version number
    :type version: str
    :param id: User&#x27;s ID
    :type id: int
    :param body: Update revenue
    :type body: dict | bytes

    :rtype: None
    """

    if check_version(version)["version"] == "error":
        return Error(error="Unauthorized"), 401

    auth_header = connexion.request.headers.get("Authorization")
    token = auth_header.split(" ")[1]
    check = check_user_auth(token)

    if check["test_key"] == "ok":
        if connexion.request.is_json:
            body = User.from_dict(connexion.request.get_json())  # noqa: E501

            session = db.Session()
            user_data = session.query(db.User).filter(db.User.id == id_).first()

            user_data.cnpj = body.cnpj
            user_data.company_name = body.company_name
            user_data.email = body.email
            user_data.name = body.name
            user_data.password = body.password
            user_data.phone_number = body.phone_number

            session.commit()
            session.close()
    else:
        return Error(error="Unauthorized"), 401


def api_vversion_users_post(version, body=None):  # noqa: E501
    """api_vversion_users_post

     # noqa: E501

    :param version: Version number
    :type version: str
    :param body: Register user
    :type body: dict | bytes

    :rtype: UserResponse
    """
    if check_version(version)["version"] == "error":
        return Error(error="Unauthorized"), 401

    auth_header = connexion.request.headers.get("Authorization")
    token = auth_header.split(" ")[1]
    check = check_user_auth(token)

    if check["test_key"] == "ok":
        if connexion.request.is_json:
            body = User.from_dict(connexion.request.get_json())  # noqa: E501

            session = db.Session()
            register = db.User(
                body.cnpj,
                body.company_name,
                body.email,
                body.name,
                body.password,
                body.phone_number,
            )
            session.add(register)
            session.commit()
            user_data = (
                session.query(db.User)
                .filter(
                    db.User.cnpj == body.cnpj,
                    db.User.company_name == body.company_name,
                    db.User.email == body.email,
                    db.User.name == body.name,
                    db.User.password == body.password,
                    db.User.phone_number == body.phone_number,
                )
                .all()
            )

            if len(user_data) > 0:
                for item in user_data:
                    response = UserResponse(user_id=item.id)
                session.close()
                return response
            else:
                return Error(error="Unauthorized"), 401
    else:
        return Error(error="Unauthorized"), 401
