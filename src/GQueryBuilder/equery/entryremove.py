from src.GQueryBuilder.equery.entryquery import EntryQuery


class EntryRemove(EntryQuery):
    """ this class represents a `DELETE` query. """
    
    def __init__(self, database):
        super().__init__(database)
    
    def build_query(self)->EntryRemove:
        """
        build the SQLite query from the EntryRemove object.

        Returns:
            EntryRemove: return the instance, allowing fluent coding.
        """
        parts = ['DELETE']
        
        if self._table: parts.append(f"FROM {self._table}")
        if self._where: parts.append(self._where)
        
        self._build_query(parts)
        return self