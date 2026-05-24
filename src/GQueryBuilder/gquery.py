import sqlite3

import src.GQueryBuilder.utils.dbtools as dbt


class GQuery:
    
    def __init__(self, database):    
        self._table: str = ""
        self._where: str = ""
        self._query = ""
        self.database = database
    
    def table(self, *args: tuple[str, ...])->GQuery:
        """
        table: set the working table.

        Returns:
            GQuery: returns the instance.
        """
        result = []
        for arg in args:
            if len(arg) == 1:
                result.append(arg[0])
            else:
                result.append(f"{arg[0]} as {arg[1]}")
        self._table = ", ".join(result)
        return self
    
    def where(self, condition: str)->GQuery:
        self._where = "WHERE " + condition
        return self
    
    def _build_query(self, parts)->str: 
        """
        build the SQLite3 query from the GQuery object.

        Returns:
            str: The SQLite3 query that can be send to any ORM.
        """
        self._query = ' '.join(parts)
    
    def run(self, receive=False):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        print(cursor.connection)
        try:
            cursor.execute(self._query)
            if receive:
                return cursor.fetchall()
            else:
                conn.commit()
        except:
            conn.rollback()