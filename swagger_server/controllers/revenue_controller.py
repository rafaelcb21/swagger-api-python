import connexion
from datetime import datetime

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.revenue import Revenue  # noqa: E501
from swagger_server.models.revenue_response import (
    RevenueResponse,
)  # noqa: E501
from swagger_server import db
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
    :param customer_id: Customer s ID
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

            session = db.Session()

            user_data = (
                session.query(db.Customer).get(customer_id)
            )

            if user_data == None:
                return Error(error='Not Found'), 404

            date_format = "%Y-%m-%d"
            register = db.Revenue(
                accrual_date=datetime.strptime(body.accrual_date, date_format),
                amount=body.amount,
                description=body.description,
                invoice_id=body.invoice_id,
                transaction_date=datetime.strptime(body.transaction_date, date_format),
                customer_id=customer_id
            )
            session.add(register)
            session.commit()

            response = RevenueResponse(revenue_id=register.id)

            session.close()

            return response, 201

        return Error(error='Unauthorized'), 401

    else:
        return Error(error='Unauthorized'), 401


def api_vversion_revenues_revenue_iddelete(version, revenue_id):  # noqa: E501
    """api_vversion_revenues_revenue_iddelete

     # noqa: E501

    :param version: Version number
    :type version: str
    :param revenue_id: Revenue s ID
    :type revenue_id: int

    :rtype: None
    """
    if check_version(version)['version'] == 'error':
        return Error(error='Unauthorized'), 401

    auth_header = connexion.request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    check = check_user_auth(token)

    if check['test_key'] == 'ok':
        session = db.Session()

        user_data = (
            session.query(db.Revenue).get(revenue_id)
        )

        if user_data == None:
            return Error(error='Not Found'), 404
        
        session.delete(user_data)
        session.commit()
        session.close()

    else:
        return Error(error='Unauthorized'), 401


def api_vversion_revenues_revenue_idput(
    version, revenue_id, body=None
):  # noqa: E501
    """api_vversion_revenues_revenue_idput

     # noqa: E501

    :param version: Version number
    :type version: str
    :param revenue_id: Revenue s ID
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
            session = db.Session()

            user_data = (
                session.query(db.Revenue).get(revenue_id)
            )

            if user_data == None:
                return Error(error='Not Found'), 404

            date_format = "%Y-%m-%d"
            
            user_data.accrual_date=datetime.strptime(body.accrual_date, date_format)
            user_data.amount=body.amount
            user_data.description=body.description
            user_data.invoice_id=body.invoice_id
            user_data.transaction_date=datetime.strptime(body.transaction_date, date_format)
                
            session.commit()
            session.close()
        
        else:
            return Error(error='Unauthorized'), 401

    else:
        return Error(error='Unauthorized'), 401
