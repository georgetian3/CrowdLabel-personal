from config import conn
cur = conn.cursor()


def correct_credentials(username, password):
    sql = "SELECT * FROM user WHERE username ='%s' and password ='%s'" % (
        username, password)
    conn.ping(reconnect=True)
    cur.execute(sql)
    conn.commit()
    result = cur.fetchall()
    if len(result) > 1:
        raise ValueError('Duplicate credentials')
    else:
        return len(result) == 1


def username_exists(username):
    sql = "SELECT * FROM user WHERE username ='%s'" % (username)
    conn.ping(reconnect=True)
    cur.execute(sql)
    conn.commit()
    result = cur.fetchall()
    if len(result) > 1:
        raise ValueError(f'Duplicate username: {str(result[0])}')
    else:
        return len(result) == 1
