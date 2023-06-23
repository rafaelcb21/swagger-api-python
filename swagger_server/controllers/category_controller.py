import connexion

from swagger_server.models.categories import Categories  # noqa: E501
from swagger_server.models.category import Category  # noqa: E501
from swagger_server.models.category_response import (
    CategoryResponse,
)  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server import db
from swagger_server.controllers.authorization_controller import (
    check_user_auth,
    check_version,
)


def api_vversion_categories_category_id_archives_put(
    version, category_id
):  # noqa: E501
    """api_vversion_categories_category_id_archives_put

     # noqa: E501

    :param version: Version number
    :type version: str
    :param category_id: Category s ID
    :type category_id: int

    :rtype: None
    """
    if check_version(version)['version'] == 'error':
        return Error(error='Unauthorized'), 401

    auth_header = connexion.request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    check = check_user_auth(token)

    if check['test_key'] == 'ok':
        session = db.Session()
        user_data = session.query(db.Category).get(category_id)

        if user_data is None:
            return Error(error='Not Found'), 404

        user_data.archive = True

        session.commit()
        session.close()

    else:
        return Error(error='Unauthorized'), 401


def api_vversion_categories_category_idget(version, category_id):  # noqa: E501
    """api_vversion_categories_category_idget

     # noqa: E501

    :param version: Version number
    :type version: str
    :param category_id: Category s ID
    :type category_id: int

    :rtype: Category
    """
    if check_version(version)['version'] == 'error':
        return Error(error='Unauthorized'), 401

    auth_header = connexion.request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    check = check_user_auth(token)

    if check['test_key'] == 'ok':
        session = db.Session()
        user_data = session.query(db.Category).get(category_id)

        if user_data is None:
            return Error(error='Not Found'), 404

        response = Category(
            description=user_data.description, name=user_data.name
        )

        session.close()

        return response, 200

    else:
        return Error(error='Unauthorized'), 401


def api_vversion_categories_category_idput(
    version, category_id, body=None
):  # noqa: E501
    """api_vversion_categories_category_idput

     # noqa: E501

    :param version: Version number
    :type version: str
    :param category_id: Category s ID
    :type category_id: int
    :param body: Update category
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
            body = Category.from_dict(
                connexion.request.get_json()
            )  # noqa: E501

            session = db.Session()
            user_data = session.query(db.Category).get(category_id)

            if user_data is None:
                return Error(error='Not Found'), 404

            user_data.description = body.description
            user_data.name = body.name

            session.commit()
            session.close()

    else:
        return Error(error='Unauthorized'), 401


def api_vversion_categories_get(version, name=None):  # noqa: E501
    """api_vversion_categories_get

     # noqa: E501

    :param version: Version number
    :type version: str
    :param name: Category s name
    :type name: str

    :rtype: Categories
    """
    if check_version(version)['version'] == 'error':
        return Error(error='Unauthorized'), 401

    auth_header = connexion.request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    check = check_user_auth(token)

    if check['test_key'] == 'ok':
        session = db.Session()

        if name is None:
            user_data = session.query(db.Category).all()
        else:
            user_data = (
                session.query(db.Category)
                .filter(db.Category.name == name)
                .all()
            )

        if len(user_data) == 0:
            return Error(error='Not Found'), 404

        elif len(user_data) > 0:
            categories = list()

            for i in user_data:
                categories.append(
                    Category(name=i.name, description=i.description)
                )

            response = Categories(count=len(categories), categories=categories)
            session.close()

            return response, 201

    else:
        return Error(error='Unauthorized'), 401


def api_vversion_categories_post(version, body=None):  # noqa: E501
    """api_vversion_categories_post

     # noqa: E501

    :param version: Version number
    :type version: str
    :param body: Register category
    :type body: dict | bytes

    :rtype: CategoryResponse
    """
    if check_version(version)['version'] == 'error':
        return Error(error='Unauthorized'), 401

    auth_header = connexion.request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    check = check_user_auth(token)

    if check['test_key'] == 'ok':
        if connexion.request.is_json:
            body = Category.from_dict(
                connexion.request.get_json()
            )  # noqa: E501
            session = db.Session()
            register = db.Category(
                name=body.name, description=body.description
            )
            session.add(register)
            session.commit()

            response = CategoryResponse(category_id=register.id)
            session.close()

            return response, 201

        return Error(error='Unauthorized'), 401

    else:
        return Error(error='Unauthorized'), 401
