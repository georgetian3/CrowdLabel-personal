from config import conn
cur = conn.cursor()


def is_existed(username, password):
    sql = "SELECT * FROM user WHERE username ='%s' and password ='%s'" % (
        username, password)
    conn.ping(reconnect=True)
    cur.execute(sql)
    conn.commit()
    result = cur.fetchall()
    if (len(result) == 0):
        return False
    else:
        return True


def exist_user(username):
    sql = "SELECT * FROM user WHERE username ='%s'" % (username)
    conn.ping(reconnect=True)
    cur.execute(sql)
    conn.commit()
    result = cur.fetchall()
    if (len(result) == 0):
        return False
    else:
        return True
