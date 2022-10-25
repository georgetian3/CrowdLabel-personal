from ast import Pass
from checkers.user import check_username
from config import conn
from checkers.user import *

from argon2 import PasswordHasher
hasher = PasswordHasher()

cur = conn.cursor()

def register(username, password, email):

    if not check_username(username):
        return 'username'
    if not check_password(password):
        return 'password'
    if not check_email(email):
        return 'email'

    password = hasher.hash(password)

    sql = "INSERT INTO user(id, username, password) VALUES ('%s','%s','%s')" % (
        0, username, password)

    cur.execute(sql)
    # commit
    conn.commit()  # 对数据库内容有改变，需要commit()
    conn.close()

    return 'ok'