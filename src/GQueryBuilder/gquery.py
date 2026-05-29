import sqlite3

# import src.GQueryBuilder.utils.dbtools as dbt
import src.GQueryBuilder.utils.dbase as utils


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
    
    def run(self, receive: bool):
        """
        run the query to the database

        Attributes:
            receive (bool, optional): precise if data will be received or not. Defaults to False.
        """
        utils.run(self.database, self._query, receive)