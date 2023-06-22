#!/usr/bin/env python3

import connexion

from swagger_server import encoder
from swagger_server import db


def main():
    db.Base.metadata.create_all(db.engine)

    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api(
        'swagger.yaml',
        arguments={'title': 'Invoice Management'},
        pythonic_params=True,
    )

    app.run(port=8080)


if __name__ == '__main__':
    main()
