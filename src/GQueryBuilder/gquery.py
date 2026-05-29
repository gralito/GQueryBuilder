import sqlite3

import src.GQueryBuilder.utils.dbtools as dbt


class GQuery:
    """
    this class is a parent class of differents query types (SELECT, UPDATE, ...).
    
    Attributes:
        _table (str): the name of the working table in the database.
        _where (str): the condition to precise the query.
        _query (str): the SQLite query sent to the database by the `run()` method.
        database (str): the path to the working database.
    """
    def __init__(self, database):    
        self._table: str = ""
        self._where: str = ""
        self._query = ""
        self.database = database
    
    def table(self, *args: tuple[str, ...])->GQuery:
        """
        set the working table(s).

        Args:
            *args (tuple[str, ...]): tuples, each one contains the name of the table and eventually an alias.
        
        Returns:
            GQuery: return the instance, allowing fluent coding.
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
        """
        define a condition to precise the query, the `WHERE` part of a query.
        
        Args:
            condition (str): a logic statement like `"name = <value>"`. can be a complex condition.

        Returns:
            GQuery: return the instance, allowing fluent coding.
        """
        self._where = "WHERE " + condition
        
        return self
    
    def _build_query(self, parts)->str: 
        """
        build the SQLite query from the parts provided by the subclass instance. called in the `build_query()` method of the subclass.

        Args:
            parts (str[]): the parts of the query in an array, sorted by the subclass method build_query().
        """
        self._query = ' '.join(parts)
    
    def run(self, receive=False):
        """
        create a connection to the database in the database attribute and send the built query.  

        Args:
            receive (bool, optional): tell if data has to be received (a SELECT query by example).

        Returns:
            Array | None: the values returned by the SQLite query or nothing.
        """
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        try:
            cursor.execute(self._query)
            if receive:
                return cursor.fetchall()
            else:
                conn.commit()
        except:
            conn.rollback()