from src.GQueryBuilder.gquery import GQuery


class EntryQuery(GQuery):
    """
    Parent class

    Attributes:
        _table (str): the name of the working table in the database.
        _where (str): the condition to precise the query.
    """
    
    self._table: str = ""
    self._where: str = ""
    
    def table(self, *args: tuple[str, ...])->EntryQuery:
        """
        set the working table(s).

        Args:
            *args (tuple[str, ...]): tuples, each one contains the name of the table and eventually an alias.
        
        Returns:
            EntryQuery: return the instance, allowing fluent coding.
        """
        result = []
        
        for arg in args:
            if len(arg) == 1:
                result.append(arg[0])
            else:
                result.append(f"{arg[0]} as {arg[1]}")
        self._table = ", ".join(result)
        
        return self
    
    def where(self, condition: str)->EntryQuery:
        """
        define a condition to precise the query, the `WHERE` part of a query.
        
        Args:
            condition (str): a logic statement like `"name = <value>"`. can be a complex condition.

        Returns:
            EntryQuery: return the instance, allowing fluent coding.
        """
        self._where = "WHERE " + condition
        
        return self