from config import conn

cur = conn.cursor()


def add_user(username, password):
    sql = "INSERT INTO user(id, username, password) VALUES ('%s','%s','%s')" % (
        0, username, password)

    cur.execute(sql)
    # commit
    conn.commit()  # 对数据库内容有改变，需要commit()
    conn.close()
