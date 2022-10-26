from checkers.user import check_username
from config import conn
from checkers.user import *

from argon2 import PasswordHasher
hasher = PasswordHasher()

cur = conn.cursor()


def register_add_user(username, password, usertype, email, status):
    if not check_username(username):
        print('username')
        return 'username'
    if not check_password(password):
        print('password')
        return 'password'
    if not check_email(email):
        print('email')
        return 'email'
    print(password)
    password = hasher.hash(password)
    sql = "INSERT INTO user(username, password, usertype,email,status) VALUES ('%s','%s','%s','%s','%s')" % (
        username, password, usertype, email, status)
    cur.execute(sql)
    # commit
    conn.commit()  # 对数据库内容有改变，需要commit()
    conn.close()
    print("ok")
    return 'ok'
