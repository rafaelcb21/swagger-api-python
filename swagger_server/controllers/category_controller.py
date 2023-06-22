import connexion
import six

from swagger_server.models.categories import Categories  # noqa: E501
from swagger_server.models.category import Category  # noqa: E501
from swagger_server.models.category_response import CategoryResponse  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server import util
from swagger_server.models.error import Error
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
    :param category_id: Category&#x27;s ID
    :type category_id: int

    :rtype: None
    """
    if check_version(version)["version"] == "error":
        return Error(error="Unauthorized"), 401

    auth_header = connexion.request.headers.get("Authorization")
    token = auth_header.split(" ")[1]
    check = check_user_auth(token)

    if check["test_key"] == "ok":
        return "do some magic!"

    else:
        return Error(error="Unauthorized"), 401


def api_vversion_categories_category_idget(version, category_id):  # noqa: E501
    """api_vversion_categories_category_idget

     # noqa: E501

    :param version: Version number
    :type version: str
    :param category_id: Category&#x27;s ID
    :type category_id: int

    :rtype: Category
    """
    if check_version(version)["version"] == "error":
        return Error(error="Unauthorized"), 401

    auth_header = connexion.request.headers.get("Authorization")
    token = auth_header.split(" ")[1]
    check = check_user_auth(token)

    if check["test_key"] == "ok":
        return "do some magic!"

    else:
        return Error(error="Unauthorized"), 401


def api_vversion_categories_category_idput(
    version, category_id, body=None
):  # noqa: E501
    """api_vversion_categories_category_idput

     # noqa: E501

    :param version: Version number
    :type version: str
    :param category_id: Category&#x27;s ID
    :type category_id: int
    :param body: Update category
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
            body = Category.from_dict(connexion.request.get_json())  # noqa: E501
        return "do some magic!"

    else:
        return Error(error="Unauthorized"), 401


def api_vversion_categories_get(version, name=None):  # noqa: E501
    """api_vversion_categories_get

     # noqa: E501

    :param version: Version number
    :type version: str
    :param name: Category&#x27;s name
    :type name: str

    :rtype: Categories
    """
    if check_version(version)["version"] == "error":
        return Error(error="Unauthorized"), 401

    auth_header = connexion.request.headers.get("Authorization")
    token = auth_header.split(" ")[1]
    check = check_user_auth(token)

    if check["test_key"] == "ok":
        return "do some magic!"

    else:
        return Error(error="Unauthorized"), 401


def api_vversion_categories_post(version, body=None):  # noqa: E501
    """api_vversion_categories_post

     # noqa: E501

    :param version: Version number
    :type version: str
    :param body: Register category
    :type body: dict | bytes

    :rtype: CategoryResponse
    """
    if check_version(version)["version"] == "error":
        return Error(error="Unauthorized"), 401

    auth_header = connexion.request.headers.get("Authorization")
    token = auth_header.split(" ")[1]
    check = check_user_auth(token)

    if check["test_key"] == "ok":
        if connexion.request.is_json:
            body = Category.from_dict(connexion.request.get_json())  # noqa: E501
        return "do some magic!"

    else:
        return Error(error="Unauthorized"), 401
