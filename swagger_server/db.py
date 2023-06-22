from sqlalchemy import Column, Integer, String, Boolean, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///db.sqlite3")
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Setting(Base):
    __tablename__ = "Setting"

    id = Column(Integer, primary_key=True)
    max_revenue_amount = Column("max_revenue_amount", Float, autoincrement=True)
    sms_notification = Column("sms_notification", Boolean, nullable=False)
    email_notification = Column("email_notification", Boolean, nullable=False)

    def __init__(self, max_revenue_amount, sms_notification, email_notification):
        self.max_revenue_amount = max_revenue_amount
        self.sms_notification = sms_notification
        self.email_notification = email_notification


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cnpj = Column("cnpj", String(14))
    company_name = Column("company_name", String(100), nullable=False)
    email = Column("email", String(50), nullable=False)
    name = Column("name", String(50), nullable=False)
    password = Column("idade", String(256), nullable=False)
    phone_number = Column("sexo", String(25), nullable=False)

    def __init__(self, cnpj, company_name, email, name, password, phone_number):
        self.cnpj = cnpj
        self.company_name = company_name
        self.email = email
        self.name = name
        self.password = password
        self.phone_number = phone_number
