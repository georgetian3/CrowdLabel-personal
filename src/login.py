from checkers.user import check_username, check_password
from config import conn

from argon2 import PasswordHasher
hasher = PasswordHasher()

cur = conn.cursor()


def login(username: str, password: str):
    if (not check_username(username) or
        not check_password(password)):

        return False

    password = hasher.hash(password)

    sql = "SELECT * FROM user WHERE username ='%s' and password ='%s'" % (
        username, password)
    conn.ping(reconnect=True)
    cur.execute(sql)
    conn.commit()
    correct_credentials = bool(len(cur.fetchall()))

    if correct_credentials:
        pass