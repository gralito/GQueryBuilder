from src.GQueryBuilder.gquery import GQuery


class DeleteQuery(GQuery):
    """Class used to generate a DELETE query"""
    
    def __init__(self, database):
        super().__init__(database)
    
    def build_query(self)->str:
        """
        build the SQLite DELETE query using the instance attributes.

        Returns:
            str: the SQLite query, ready to use.
        """
        parts = ['DELETE']
        
        if self._table: parts.append(f"FROM {self._table}")
        if self._where: parts.append(self._where)
        
        return self._build_query(parts)