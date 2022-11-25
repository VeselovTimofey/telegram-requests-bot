import os
import sqlite3

conn = sqlite3.connect(os.path.join("db", "appeal.db"))
cursor = conn.cursor()


def get_cursor():
    return cursor


def _init_db():
    with open("create_db.sql", "r") as sql_command:
        sql = sql_command.read()
    cursor.executescript(sql)
    conn.commit()


def check_db_exists():
    cursor.execute("SELECT name FROM sqlite_master "
                   "WHERE type='table' AND name='appeal'")
    table_exists = cursor.fetchall()
    if table_exists:
        return
    _init_db()


check_db_exists()
