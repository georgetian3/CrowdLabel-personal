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
    res = con.query(User).filter(User.username == username).all()

    if (len(res) == 0):
        return False

    user = res[0]

    return hasher.verify(user.password, password)


def field_exists(field, value):
    con = scoped_session(Connection)
    res = con.query(User).filter(User.__dict__[field] == value).all()
    if len(res) > 1:
        raise ValueError(f'Duplicate username: {str(res.all()[0])}')
    else:
        return len(res) == 1

def username_exists(username):
    return field_exists('username', username)

def email_exists(email):
    return field_exists('email', email)