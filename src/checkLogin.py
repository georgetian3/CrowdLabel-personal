from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from database import User
from argon2 import PasswordHasher
hasher = PasswordHasher()
engine = create_engine(
    "mysql+pymysql://root:cxq1974328@127.0.0.1:3306/crowdlabel?charset=utf8")
Connection = sessionmaker(bind=engine)


def correct_credentials(username, password):
    con = scoped_session(Connection)
    res = con.query(User).filter(User.username == username)
    if (len(res.all()) == 0):
        return False
    user = res.all()[0]
    try:
        res = hasher.verify(user.password, password)
    except:
        res = False
    else:
        res = True

    return res


def username_exists(username):
    con = scoped_session(Connection)
    res = con.query(User).filter(User.username == username)
    if len(res.all()) > 1:
        raise ValueError(f'Duplicate username: {str(res.all()[0])}')
    else:
        return len(res.all()) == 1
