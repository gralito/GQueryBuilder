import sqlite3


def run(database: str, query: str, receive: bool = False):
    """
    create a connection to the database in the database attribute and send the built query.  

    Args:
        receive (bool, optional): tell if data has to be received (a SELECT query by example).

    Returns:
        Array | None: the values returned by the SQLite query or nothing.
    """
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        if receive:
            return cursor.fetchall()
        else:
            conn.commit()
    except:
        conn.rollback()

def create_database(path: str):
    pass