from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Float,
    Date,
    ForeignKey,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Setting(Base):
    __tablename__ = 'Setting'

    id = Column(Integer, primary_key=True)
    max_revenue_amount = Column(
        'max_revenue_amount', Float, autoincrement=True
    )
    sms_notification = Column('sms_notification', Boolean, nullable=False)
    email_notification = Column('email_notification', Boolean, nullable=False)

    def __init__(
        self, max_revenue_amount, sms_notification, email_notification
    ):
        self.max_revenue_amount = max_revenue_amount
        self.sms_notification = sms_notification
        self.email_notification = email_notification


class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cnpj = Column('cnpj', String(14), nullable=False)
    company_name = Column('company_name', String(100), nullable=False)
    email = Column('email', String(50), nullable=False)
    name = Column('name', String(50), nullable=False)
    password = Column('password', String(256), nullable=False)
    phone_number = Column('phone_number', String(25), nullable=False)

    def __init__(
        self, cnpj, company_name, email, name, password, phone_number
    ):
        self.cnpj = cnpj
        self.company_name = company_name
        self.email = email
        self.name = name
        self.password = password
        self.phone_number = phone_number


class Customer(Base):
    __tablename__ = 'Customer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cnpj = Column('cnpj', String(14), nullable=False)
    commercial_name = Column('commercial_name', String(100), nullable=False)
    legal_name = Column('legal_name', String(100), nullable=False)
    archive = Column('archive', Boolean, default=False, nullable=True)

    def __init__(self, cnpj, commercial_name, legal_name):
        self.cnpj = cnpj
        self.commercial_name = commercial_name
        self.legal_name = legal_name


class Revenue(Base):
    __tablename__ = 'Revenue'

    id = Column(Integer, primary_key=True, autoincrement=True)
    invoice_id = Column('invoice_id', String(14), nullable=False)
    accrual_date = Column('accrual_date', Date, nullable=False)
    amount = Column('amount', Float, nullable=False)
    description = Column('description', String(100), nullable=False)
    transaction_date = Column('transaction_date', Date, nullable=False)
    customer_id = Column(
        'customer_id', Integer, ForeignKey('Customer.id'), nullable=False
    )

    Customer = relationship('Customer')

    def __init__(
        self,
        invoice_id,
        accrual_date,
        amount,
        description,
        transaction_date,
        customer_id,
    ):
        self.invoice_id = invoice_id
        self.accrual_date = accrual_date
        self.amount = amount
        self.description = description
        self.transaction_date = transaction_date
        self.customer_id = customer_id


class Category(Base):
    __tablename__ = 'Category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(100), nullable=False)
    description = Column('description', String(100), nullable=False)
    archive = Column('archive', Boolean, default=False, nullable=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description


class Expense(Base):
    __tablename__ = 'Expense'

    id = Column(Integer, primary_key=True, autoincrement=True)
    accrual_date = Column('accrual_date', Date, nullable=False)
    amount = Column('amount', Float, nullable=False)
    description = Column('description', String(100), nullable=False)
    transaction_date = Column('transaction_date', Date, nullable=True)
    customer_id = Column(
        'customer_id',
        Integer,
        ForeignKey('Customer.id'),
        default=None,
        nullable=True,
    )
    category_id = Column(
        'category_id', Integer, ForeignKey('Category.id'), nullable=False
    )

    Customer = relationship('Customer')
    Category = relationship('Category')

    def __init__(
        self,
        accrual_date,
        amount,
        description,
        transaction_date,
        category_id,
        customer_id,
    ):
        self.accrual_date = accrual_date
        self.amount = amount
        self.description = description
        self.transaction_date = transaction_date
        self.category_id = category_id
        self.customer_id = customer_id
