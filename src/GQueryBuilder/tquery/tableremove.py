from src.GQueryBuilder.tquery.tablequery import TableQuery


class TableRemove(TableQuery):
    if_exists: bool
    
    def __init__(self, database: str, if_exists: bool = False):
        super().__init__(database=database)
        self.if_exists = if_exists
        
    def build_query(self)->TableRemove:
        """
        build the SQLite query from the TableRemove object.

        Returns:
            TableRemove: return the instance, allowing fluent coding.
        """
        parts = ['DROP TABLE']
        
        if self.if_exists: parts.append('IF EXISTS')
        parts.append(self._name)
        self._build_query(parts)
        return self