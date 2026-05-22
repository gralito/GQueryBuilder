from src.gquery import GQuery


class DeleteQuery(GQuery):
    """Class used to generate a DELETE query"""
    
    def build_query(self)->str:
        """
        build the SQLite DELETE query using the instance attributes.

        Returns:
            str: the SQLite query, ready to use.
        """
        parts = ['DELETE']
        
        if self._table: parts.append(self._table)
        if self._where: parts.append(self._where)
        
        return self._build_query(parts)