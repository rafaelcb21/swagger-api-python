import os
import sqlite3


def connect_database():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, 'dados.db')
    conn = sqlite3.connect(db_path)

    return conn
