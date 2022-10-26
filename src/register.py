from checkers.user import check_username
from checkers.user import *
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from database import User

from password import hash, verify

#cur = conn.cursor()

engine = create_engine(
    "mysql+pymysql://root:cxq1974328@127.0.0.1:3306/crowdlabel?charset=utf8")
Connection = sessionmaker(bind=engine)


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
    print("________")
    print(password)
    temp = password
    password = hash(password)
    print("________")
    print(password)
    verify(password, temp)
    con = scoped_session(Connection)
    user = User(username=username, password=password,
                email=email, type=usertype, status=status)
    con.add(user)
    con.commit()
    con.close()
    # sql = "INSERT INTO user(username, password, usertype,email,status) VALUES ('%s','%s','%s','%s','%s')" % (
    #    username, password, usertype, email, status)
    # cur.execute(sql)
    # commit
    # conn.commit()  # 对数据库内容有改变，需要commit()
    # conn.close()
    print("ok")
    return 'ok'
