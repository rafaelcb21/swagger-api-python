import connexion
from datetime import datetime

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.expense import Expense  # noqa: E501
from swagger_server.models.expense_response import (
    ExpenseResponse,
)  # noqa: E501
from swagger_server import db
from swagger_server.controllers.authorization_controller import (
    check_user_auth,
    check_version,
)


def api_vversion_expenses_category_idpost(
    version, category_id, body=None
):  # noqa: E501
    """api_vversion_expenses_category_idpost

     # noqa: E501

    :param version: Version number
    :type version: str
    :param category_id: Category s ID
    :type category_id: int
    :param body: Expense by category
    :type body: dict | bytes

    :rtype: ExpenseResponse
    """
    if check_version(version)['version'] == 'error':
        return Error(error='Unauthorized'), 401

    auth_header = connexion.request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    check = check_user_auth(token)

    if check['test_key'] == 'ok':
        if connexion.request.is_json:
            body = Expense.from_dict(
                connexion.request.get_json()
            )  # noqa: E501

            session = db.Session()
            user_data = session.query(db.Category).get(category_id)

            if user_data is None:
                return Error(error='Not Found'), 404

            user_data_ = session.query(db.Customer).get(body.customer_id)

            if user_data_ is None:
                body.customer_id = None

            date_format = '%Y-%m-%d'
            register = db.Expense(
                accrual_date=datetime.strptime(body.accrual_date, date_format),
                amount=body.amount,
                description=body.description,
                transaction_date=datetime.strptime(
                    body.transaction_date, date_format
                ),
                customer_id=body.customer_id,
                category_id=category_id,
            )
            session.add(register)
            session.commit()

            response = ExpenseResponse(expense_id=register.id)

            session.close()

            return response, 201

        return Error(error='Unauthorized'), 401

    else:
        return Error(error='Unauthorized'), 401


def api_vversion_expenses_expense_iddelete(version, expense_id):  # noqa: E501
    """api_vversion_expenses_expense_iddelete

     # noqa: E501

    :param version: Version number
    :type version: str
    :param expense_id: Expense s ID
    :type expense_id: int

    :rtype: None
    """
    auth_header = connexion.request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    check = check_user_auth(token)

    if check_version(version)['version'] == 'error':
        return Error(error='Unauthorized'), 401

    if check['test_key'] == 'ok':
        session = db.Session()

        user_data = session.query(db.Expense).get(expense_id)

        if user_data is None:
            return Error(error='Not Found'), 404

        session.delete(user_data)
        session.commit()
        session.close()

    else:
        return Error(error='Unauthorized'), 401


def api_vversion_expenses_expense_idput(
    version, expense_id, body=None
):  # noqa: E501
    """api_vversion_expenses_expense_idput

     # noqa: E501

    :param version: Version number
    :type version: str
    :param expense_id: Expense s ID
    :type expense_id: int
    :param body: Register expense
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
            body = Expense.from_dict(
                connexion.request.get_json()
            )  # noqa: E501

            session = db.Session()

            user_data = session.query(db.Expense).get(expense_id)

            if user_data is None:
                return Error(error='Not Found'), 404

            user_data_ = session.query(db.Customer).get(body.customer_id)

            if user_data_ is None:
                body.customer_id = None

            date_format = '%Y-%m-%d'

            user_data.accrual_date = datetime.strptime(
                body.accrual_date, date_format
            )
            user_data.amount = body.amount
            user_data.description = body.description
            user_data.transaction_date = datetime.strptime(
                body.transaction_date, date_format
            )
            user_data.customer_id = body.customer_id

            session.commit()
            session.close()

        else:
            return Error(error='Unauthorized'), 401

    else:
        return Error(error='Unauthorized'), 401
