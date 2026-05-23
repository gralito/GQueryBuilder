import src.GQueryBuilder.utils.dbtools as dbt


class GQuery:
    
    def __init__(self, database):    
        self._table: str = ""
        self._where: str = ""
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
        self._table = "FROM " + ", ".join(result)
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
        return ' '.join(parts)
    
    @classmethod
    def run(query: str, data=None, receive=False):
        # TO IMPLEMENT
        conn = sqlite3.connect("tasks.db")
        cursor = conn.cursor()
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        if receive:
            return cursor.fetchall()
        else:
            conn.commit()        