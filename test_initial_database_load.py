import datetime

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

from sqlalchemy.orm import sessionmaker, relationship, declarative_base

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


# Initiate the load in database
session = Session()

# SETTING COMMIT
setting = [
    {
        'email_notification': True,
        'max_revenue_amount': 81000.0,
        'sms_notification': False,
    }
]

for i in setting:
    register = Setting(
        email_notification=i['email_notification'],
        max_revenue_amount=i['max_revenue_amount'],
        sms_notification=i['sms_notification'],
    )
    session.add(register)
    session.commit()


# USER COMMIT
user = [
    {
        'cnpj': '47563936000194',
        'company_name': 'MyCompany',
        'email': 'my_company@dev.com.br',
        'name': 'admin',
        'password': 'admin',
        'phone_number': '1199998888',
    }
]

for i in user:
    register = User(
        cnpj=i['cnpj'],
        company_name=i['company_name'],
        email=i['email'],
        name=i['name'],
        password=i['password'],
        phone_number=i['phone_number'],
    )
    session.add(register)
    session.commit()

# CUSTOMER COMMIT
customer = [
    {
        'cnpj': '80663676000102',
        'commercial_name': 'Google',
        'legal_name': 'Alphabet',
    },
    {
        'cnpj': '80663676000104',
        'commercial_name': 'Apple',
        'legal_name': 'Apple Computer, Inc',
    },
    {
        'cnpj': '80663676222109',
        'commercial_name': 'OpenAI',
        'legal_name': 'OpenAI Incorporated',
    },
    {
        'cnpj': '80663676222105',
        'commercial_name': 'Microsoft',
        'legal_name': 'Microsoft Corporation',
    },
    {
        'cnpj': '30663676000102',
        'commercial_name': 'Adobe',
        'legal_name': 'Adobe Systems Incorporated',
    },
]

for i in customer:
    register = Customer(
        cnpj=i['cnpj'],
        commercial_name=i['commercial_name'],
        legal_name=i['legal_name'],
    )
    session.add(register)
    session.commit()

# CATEGORY COMMIT
category = [
    {
        'description': 'Despesa relacionada a alimentação',
        'name': 'Alimentação',
    },
    {'description': 'Despesa relacionada a transporte', 'name': 'Transporte'},
    {'description': 'Despesa relacionada a moradia', 'name': 'Moradia'},
    {'description': 'Despesa relacionada a saúde', 'name': 'Saúde'},
    {'description': 'Receita proveniente de salário', 'name': 'Salário'},
    {'description': 'Receita proveniente de vendas', 'name': 'Vendas'},
    {
        'description': 'Receita proveniente de investimentos',
        'name': 'Investimentos',
    },
    {'description': 'Receita proveniente de aluguel', 'name': 'Aluguel'},
]

for i in category:
    register = Category(name=i['name'], description=i['description'])
    session.add(register)
    session.commit()

# REVENUE COMMIT
revenue = [
    {
        'accrual_date': datetime.date(2023, 1, 1),
        'amount': 10,
        'description': 'carro',
        'invoice_id': '123456',
        'transaction_date': datetime.date(2023, 2, 2),
        'customer_id': 1,
    },
    {
        'accrual_date': datetime.date(2023, 1, 2),
        'amount': 10,
        'description': 'carro',
        'invoice_id': '123456',
        'transaction_date': datetime.date(2023, 2, 2),
        'customer_id': 1,
    },
    {
        'accrual_date': datetime.date(2023, 2, 3),
        'amount': 10,
        'description': 'carro',
        'invoice_id': '123456',
        'transaction_date': datetime.date(2023, 2, 2),
        'customer_id': 1,
    },
    {
        'accrual_date': datetime.date(2023, 2, 1),
        'amount': 10,
        'description': 'carro',
        'invoice_id': '123456',
        'transaction_date': datetime.date(2023, 2, 2),
        'customer_id': 1,
    },
    {
        'accrual_date': datetime.date(2023, 3, 1),
        'amount': 10,
        'description': 'carro',
        'invoice_id': '123456',
        'transaction_date': datetime.date(2023, 2, 2),
        'customer_id': 1,
    },
    {
        'accrual_date': datetime.date(2023, 3, 1),
        'amount': 10,
        'description': 'carro',
        'invoice_id': '123456',
        'transaction_date': datetime.date(2023, 2, 2),
        'customer_id': 1,
    },
    {
        'accrual_date': datetime.date(2023, 4, 1),
        'amount': 10,
        'description': 'carro',
        'invoice_id': '123456',
        'transaction_date': datetime.date(2023, 2, 2),
        'customer_id': 2,
    },
    {
        'accrual_date': datetime.date(2023, 4, 1),
        'amount': 10,
        'description': 'carro',
        'invoice_id': '123456',
        'transaction_date': datetime.date(2023, 2, 2),
        'customer_id': 2,
    },
    {
        'accrual_date': datetime.date(2023, 5, 1),
        'amount': 10,
        'description': 'carro',
        'invoice_id': '123456',
        'transaction_date': datetime.date(2023, 2, 2),
        'customer_id': 2,
    },
    {
        'accrual_date': datetime.date(2023, 5, 1),
        'amount': 10,
        'description': 'carro',
        'invoice_id': '123456',
        'transaction_date': datetime.date(2023, 2, 2),
        'customer_id': 2,
    },
    {
        'accrual_date': datetime.date(2023, 6, 1),
        'amount': 10,
        'description': 'carro',
        'invoice_id': '123456',
        'transaction_date': datetime.date(2023, 2, 2),
        'customer_id': 2,
    },
    {
        'accrual_date': datetime.date(2023, 6, 1),
        'amount': 10,
        'description': 'carro',
        'invoice_id': '123456',
        'transaction_date': datetime.date(2023, 2, 2),
        'customer_id': 2,
    },
    {
        'accrual_date': datetime.date(2023, 7, 1),
        'amount': 10,
        'description': 'carro',
        'invoice_id': '123456',
        'transaction_date': datetime.date(2023, 2, 2),
        'customer_id': 3,
    },
    {
        'accrual_date': datetime.date(2023, 7, 1),
        'amount': 10,
        'description': 'carro',
        'invoice_id': '123456',
        'transaction_date': datetime.date(2023, 2, 2),
        'customer_id': 3,
    },
    {
        'accrual_date': datetime.date(2023, 8, 1),
        'amount': 10,
        'description': 'carro',
        'invoice_id': '123456',
        'transaction_date': datetime.date(2023, 2, 2),
        'customer_id': 3,
    },
    {
        'accrual_date': datetime.date(2023, 8, 1),
        'amount': 10,
        'description': 'carro',
        'invoice_id': '123456',
        'transaction_date': datetime.date(2023, 2, 2),
        'customer_id': 3,
    },
    {
        'accrual_date': datetime.date(2023, 9, 1),
        'amount': 10,
        'description': 'carro',
        'invoice_id': '123456',
        'transaction_date': datetime.date(2023, 2, 2),
        'customer_id': 3,
    },
    {
        'accrual_date': datetime.date(2023, 9, 1),
        'amount': 10,
        'description': 'carro',
        'invoice_id': '123456',
        'transaction_date': datetime.date(2023, 2, 2),
        'customer_id': 3,
    },
    {
        'accrual_date': datetime.date(2023, 10, 1),
        'amount': 10,
        'description': 'carro',
        'invoice_id': '123456',
        'transaction_date': datetime.date(2023, 2, 2),
        'customer_id': 4,
    },
    {
        'accrual_date': datetime.date(2023, 10, 1),
        'amount': 10,
        'description': 'carro',
        'invoice_id': '123456',
        'transaction_date': datetime.date(2023, 2, 2),
        'customer_id': 4,
    },
    {
        'accrual_date': datetime.date(2023, 11, 1),
        'amount': 10,
        'description': 'carro',
        'invoice_id': '123456',
        'transaction_date': datetime.date(2023, 2, 2),
        'customer_id': 4,
    },
    {
        'accrual_date': datetime.date(2023, 11, 1),
        'amount': 10,
        'description': 'carro',
        'invoice_id': '123456',
        'transaction_date': datetime.date(2023, 2, 2),
        'customer_id': 4,
    },
    {
        'accrual_date': datetime.date(2023, 12, 1),
        'amount': 10,
        'description': 'carro',
        'invoice_id': '123456',
        'transaction_date': datetime.date(2023, 2, 2),
        'customer_id': 4,
    },
    {
        'accrual_date': datetime.date(2023, 12, 1),
        'amount': 10,
        'description': 'carro',
        'invoice_id': '123456',
        'transaction_date': datetime.date(2023, 2, 2),
        'customer_id': 4,
    },
    {
        'accrual_date': datetime.date(2024, 12, 1),
        'amount': 10,
        'description': 'carro',
        'invoice_id': '123456',
        'transaction_date': datetime.date(2024, 2, 2),
        'customer_id': 5,
    },
    {
        'accrual_date': datetime.date(2024, 12, 1),
        'amount': 10,
        'description': 'carro',
        'invoice_id': '123456',
        'transaction_date': datetime.date(2024, 2, 2),
        'customer_id': 5,
    },
]

for i in revenue:
    register = Revenue(
        accrual_date=i['accrual_date'],
        amount=i['amount'],
        description=i['description'],
        invoice_id=i['invoice_id'],
        transaction_date=i['transaction_date'],
        customer_id=i['customer_id'],
    )
    session.add(register)
    session.commit()

# EXPENSE COMMIT
expense = [
    {
        'accrual_date': datetime.date(2023, 1, 3),
        'amount': 900,
        'customer_id': 1,
        'description': 'materiais de escritorio',
        'transaction_date': datetime.date(2023, 1, 9),
        'category_id': 2,
    },
    {
        'accrual_date': datetime.date(2023, 2, 3),
        'amount': 800000.0,
        'customer_id': 2,
        'description': 'frota de carros',
        'transaction_date': datetime.date(2023, 2, 9),
        'category_id': 3,
    },
    {
        'accrual_date': datetime.date(2023, 3, 3),
        'amount': 5000.0,
        'customer_id': 3,
        'description': 'energia eletrica',
        'transaction_date': datetime.date(2023, 4, 9),
        'category_id': 4,
    },
]

for i in expense:
    register = Expense(
        accrual_date=i['accrual_date'],
        amount=i['amount'],
        customer_id=i['customer_id'],
        description=i['description'],
        transaction_date=i['transaction_date'],
        category_id=i['category_id'],
    )
    session.add(register)
    session.commit()

session.close()
