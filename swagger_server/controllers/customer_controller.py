import connexion
import six

from swagger_server.models.customer import Customer  # noqa: E501
from swagger_server.models.customer_response import (
    CustomerResponse,
)  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.get_customer import GetCustomer  # noqa: E501
from swagger_server.models.get_customers import GetCustomers  # noqa: E501
from swagger_server import db
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
    :param customer_id: Customer s ID
    :type customer_id: int

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
            session.query(db.Customer).filter(db.Customer.id == customer_id).first()
        )

        if user_data == None:
            return Error(error='Not Found'), 404

        user_data.archive = True

        session.commit()
        session.close()

    else:
        return Error(error='Unauthorized'), 401


def api_vversion_customers_customer_idget(version, customer_id):  # noqa: E501
    """api_vversion_customers_customer_idget

     # noqa: E501

    :param version: Version number
    :type version: str
    :param customer_id: Customer s ID
    :type customer_id: int

    :rtype: GetCustomer
    """
    if check_version(version)['version'] == 'error':
        return Error(error='Unauthorized'), 401

    auth_header = connexion.request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    check = check_user_auth(token)

    if check['test_key'] == 'ok':
        session = db.Session()
        user_data = session.query(db.Customer).filter(db.Customer.id == customer_id).first()

        if user_data == None:
            return Error(error='Not Found'), 404
        
        response = GetCustomer(
            customer=Customer(
                cnpj=user_data.cnpj,
                commercial_name=user_data.commercial_name,
                legal_name=user_data.legal_name
            )
        )

        session.close()

        return response, 200

    else:
        return Error(error='Unauthorized'), 401


def api_vversion_customers_customer_idput(version, customer_id, body=None):  # noqa: E501
    """api_vversion_customers_customer_idput

     # noqa: E501

    :param version: Version number
    :type version: str
    :param customer_id: Customer s ID
    :type customer_id: int

    :rtype: None
    """

    if check_version(version)['version'] == 'error':
        return Error(error='Unauthorized'), 401

    auth_header = connexion.request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    check = check_user_auth(token)

    if check['test_key'] == 'ok':
        if connexion.request.is_json:
            body = Customer.from_dict(connexion.request.get_json())  # noqa: E501

            session = db.Session()
            user_data = (
                session.query(db.Customer).filter(db.Customer.id == customer_id).first()
            )

            if user_data == None:
                return Error(error='Not Found'), 404
            
            user_data.cnpj = body.cnpj
            user_data.commercial_name = body.commercial_name
            user_data.legal_name = body.legal_name

            session.commit()
            session.close()

    else:
        return Error(error='Unauthorized'), 401


def api_vversion_customers_get(version, name=None, cnpj=None):  # noqa: E501
    """api_vversion_customers_get

     # noqa: E501

    :param version: Version number
    :type version: str
    :param name: Customer s name
    :type name: str
    :param cnpj: Customer s cnpj
    :type cnpj: str

    :rtype: GetCustomers
    """
    if check_version(version)['version'] == 'error':
        return Error(error='Unauthorized'), 401

    auth_header = connexion.request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    check = check_user_auth(token)

    if check['test_key'] == 'ok':
        session = db.Session()

        if name is None and cnpj is None:
            user_data = session.query(db.Customer).all()
        elif name is None and cnpj is not None:
            user_data = session.query(db.Customer).filter(db.Customer.cnpj == cnpj).all()
        elif name is not None and cnpj is None:
            user_data = session.query(db.Customer).filter(db.Customer.commercial_name == name).all()
        elif name is not None and cnpj is not None:
            user_data = session.query(db.Customer).filter(db.Customer.commercial_name == name, db.Customer.cnpj == cnpj).all()
        
        if len(user_data) == 0:
            return Error(error='Not Found'), 404

        elif len(user_data) > 0:
            customers = list()

            for i in user_data:
                customers.append(Customer(cnpj=i.cnpj, commercial_name=i.commercial_name, legal_name=i.legal_name))

            response = GetCustomers(
                count=len(customers),
                customers=customers)
            session.close()

            return response, 201

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

            session = db.Session()
            register = db.Customer(
                cnpj=body.cnpj,
                commercial_name=body.commercial_name,
                legal_name=body.legal_name
            )
            session.add(register)
            session.commit()

            user_data = (
                session.query(db.Customer)
                .filter(
                    db.Customer.cnpj == body.cnpj,
                    db.Customer.commercial_name == body.commercial_name,
                    db.Customer.legal_name == body.legal_name
                )
                .first()
            )

            response = CustomerResponse(customer_id=user_data.id)

            return response, 201

        return Error(error='Unauthorized'), 401

    else:
        return Error(error='Unauthorized'), 401
