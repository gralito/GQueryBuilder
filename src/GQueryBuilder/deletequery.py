from src.GQueryBuilder.gquery import GQuery


class DeleteQuery(GQuery):
    """ this class represents a `DELETE` query. """
    
    def __init__(self, database):
        super().__init__(database)
    
    def build_query(self)->DeleteQuery:
        """
        build the SQLite query from the DeleteQuery object.

        Returns:
            DeleteQuery: return the instance, allowing fluent coding.
        """
        parts = ['DELETE']
        
        if self._table: parts.append(f"FROM {self._table}")
        if self._where: parts.append(self._where)
        
        self._build_query(parts)
        return self