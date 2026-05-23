@staticmethod
def runQuery(sql, data=None, receive=False):
    # TO IMPLEMENT
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    if data:
        cursor.execute(sql, data)
    else:
        cursor.execute(sql)
    if receive:
        return cursor.fetchall()
    else:
        conn.commit()  