import sqlite3

# import src.GQueryBuilder.utils.dbtools as dbt
from src.GQueryBuilder.utils.dbase import run as db_run


class GQuery:
    """
    this class is the mother class of all query types (SELECT, UPDATE, ...).
    
    Attributes:
        _query (str): the SQLite query sent to the database by the `run()` method.
        database (str): the path to the working database.
    """
    def __init__(self, database):    
        
        self._query = ""
        self.database = database
    
    
    
    def _build_query(self, parts)->str: 
        """
        build the SQLite query from the parts provided by the subclass instance. called in the `build_query()` method of the subclass.

        Args:
            parts (str[]): the parts of the query in an array, sorted by the subclass method build_query().
        """
        self._query = ' '.join(parts)
        return self
    
    def run(self, receive: bool = False):
        """
        run the query to the database

        Attributes:
            receive (bool, optional): precise if data will be received or not. Defaults to False.
        """
        return db_run(self.database, self._query, receive)