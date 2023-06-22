import connexion
from sqlalchemy import extract, func

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.fiscal_year import FiscalYear  # noqa: E501

from swagger_server.models.revenue_by_customer import RevenueByCustomer  # noqa: E501
from swagger_server.models.revenue_by_month import RevenueByMonth  # noqa: E501
from swagger_server.models.month_revenue import MonthRevenue  # noqa: E501
from swagger_server.models.customer_revenue import CustomerRevenue  # noqa: E501
from swagger_server.models.total_revenue import TotalRevenue  # noqa: E501
from swagger_server import db
from swagger_server.models.error import Error
from swagger_server.controllers.authorization_controller import (
    check_user_auth,
    check_version,
)

import calendar
import locale


def api_vversion_reports_revenue_by_customer_post(
    version, body=None
):  # noqa: E501
    """api_vversion_reports_revenue_by_customer_post

     # noqa: E501

    :param version: Version number
    :type version: str
    :param body: Fiscal Year
    :type body: dict | bytes

    :rtype: RevenueByCustomer
    """
    if check_version(version)['version'] == 'error':
        return Error(error='Unauthorized'), 401

    auth_header = connexion.request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    check = check_user_auth(token)

    if check['test_key'] == 'ok':
        if connexion.request.is_json:
            body = FiscalYear.from_dict(
                connexion.request.get_json()
            )  # noqa: E501

            session = db.Session()

            year = body.fiscal_year

            result = session.query(
                db.Customer.commercial_name.label('customer_name'), 
                func.sum(db.Revenue.amount).label('revenue')).\
                join(db.Revenue).\
                filter(func.extract('year', db.Revenue.accrual_date) == year).\
                group_by(db.Customer.commercial_name).all()

            revenue_list = []
            for row in result:
                revenue_obj = CustomerRevenue(
                    customer_name=row.customer_name,
                    revenue=row.revenue
                )
                revenue_list.append(revenue_obj)

            user_data = (
                session.query(db.Setting).first()
            )

            if user_data != None:
                max_revenue_amount = user_data.max_revenue_amount
            else:
                max_revenue_amount = 0

            response = RevenueByCustomer(
                max_revenue_amount=max_revenue_amount,
                revenue=revenue_list
            )

            return response, 201

        return Error(error='Unauthorized'), 401

    else:
        return Error(error='Unauthorized'), 401


def api_vversion_reports_revenue_by_month_post(
    version, body=None
):  # noqa: E501
    """api_vversion_reports_revenue_by_month_post

     # noqa: E501

    :param version: Version number
    :type version: str
    :param body: Fiscal Year
    :type body: dict | bytes

    :rtype: RevenueByMonth
    """
    if check_version(version)['version'] == 'error':
        return Error(error='Unauthorized'), 401

    auth_header = connexion.request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    check = check_user_auth(token)

    if check['test_key'] == 'ok':
        if connexion.request.is_json:
            body = FiscalYear.from_dict(
                connexion.request.get_json()
            )  # noqa: E501

            session = db.Session()

            year = body.fiscal_year

            result = session.query(
                extract('month', db.Revenue.accrual_date).label('month'),
                func.sum(db.Revenue.amount).label('month_revenue')
            ).filter(extract('year', db.Revenue.accrual_date) == year).group_by(extract('month', db.Revenue.accrual_date)).all()

            result_list = []

            for row in result:
                locale.setlocale(locale.LC_ALL, 'pt_BR')
                month_name = calendar.month_name[row[0]]
                month_revenue = row[1]

                item = MonthRevenue(
                    month_name=month_name,
                    month_revenue=month_revenue
                ) 
                
                result_list.append(item)

            user_data = (
                session.query(db.Setting).first()
            )

            if user_data != None:
                max_revenue_amount = user_data.max_revenue_amount
            else:
                max_revenue_amount = 0

            response = RevenueByMonth(
                revenue=result_list,
                max_revenue_amount=max_revenue_amount
            )

            session.close()

            return response, 201
        
        return Error(error='Unauthorized'), 401

    else:
        return Error(error='Unauthorized'), 401


def api_vversion_reports_total_revenue_post(version, body=None):  # noqa: E501
    """api_vversion_reports_total_revenue_post

     # noqa: E501

    :param version: Version number
    :type version: str
    :param body: Register customer
    :type body: dict | bytes

    :rtype: TotalRevenue
    """
    if check_version(version)['version'] == 'error':
        return Error(error='Unauthorized'), 401

    auth_header = connexion.request.headers.get('Authorization')
    token = auth_header.split(' ')[1]
    check = check_user_auth(token)

    if check['test_key'] == 'ok':
        if connexion.request.is_json:
            body = FiscalYear.from_dict(
                connexion.request.get_json()
            )  # noqa: E501
            session = db.Session()

            year = body.fiscal_year

            total_revenue = session.query(
                func.sum(db.Revenue.amount).label('total_revenue')
            ).filter(
                func.extract('year', db.Revenue.accrual_date) == year
            ).scalar()

            user_data = (
                session.query(db.Setting).first()
            )

            if user_data != None:
                max_revenue_amount = user_data.max_revenue_amount
            else:
                max_revenue_amount = 0

            response = TotalRevenue(
                total_revenue=total_revenue,
                max_revenue_amount=max_revenue_amount
            )

            session.close()

            return response, 201
        
        return Error(error='Unauthorized'), 401

    else:
        return Error(error='Unauthorized'), 401
