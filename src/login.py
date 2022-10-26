from checkers.user import check_username, check_password
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from database import User
from sqlalchemy import and_

from password import hash

engine = create_engine(
    "mysql+pymysql://root:cxq1974328@127.0.0.1:3306/crowdlabel?charset=utf8")
Connection = sessionmaker(bind=engine)


def login(username: str, password: str):
    if (not check_username(username) or
            not check_password(password)):

        return False

    password = hash(password)
    con = scoped_session(Connection)
    res = con.query(User).filter(
        and_(User.username == username, User.password == password))
    correct_credentials = bool(len(res.all()))

    if correct_credentials:
        return "ok"
    else:
        return "false"
