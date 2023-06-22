from typing import List
from pathlib import Path
import jwt
import os
from dotenv import load_dotenv
from swagger_server.models.error import Error  # noqa: E501


env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(env_path)
"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""

ssh_path = Path(__file__).resolve().parent.parent.parent / ".ssh"


def check_user_auth(token):
    secret_key = os.environ.get("SECRET_KEY")
    try:
        decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])
        return {"test_key": "ok", "decoded_token": decoded_token}

    except jwt.exceptions.DecodeError:
        return {"test_key": "error"}

    except jwt.exceptions.InvalidTokenError:
        return {"test_key": "error"}


def check_version(version):
    v = os.environ.get("VERSION")
    if version != v:
        return {"version": "error"}
    return {"version": "ok"}
