#!/usr/bin/env python3

import connexion

from swagger_server import encoder
from swagger_server import db


def main():
    db.Base.metadata.create_all(db.engine)

    app = connexion.App(__name__, specification_dir="./swagger/")
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api(
        "swagger.yaml", arguments={"title": "Invoice Management"}, pythonic_params=True
    )

    # session = db.Session()
    # setting = db.User(
    #    '47563936000194', 'MyCompany', 'my_company@dev.com.br',
    #    'admin', 'admin', '1199998888'
    # )
    # setting = db.Setting(81000, True, True)
    # session.add(setting)
    # session.commit()
    # dados = session.query(db.User).all()
    # print(dados)
    # for linha in dados:
    #    print(f'Max: {linha.max_revenue_amount} - SMS: {linha.sms_notification} - EMAIL: {linha.email_notification}')

    app.run(port=8080)


if __name__ == "__main__":
    main()
