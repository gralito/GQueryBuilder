


class GQuery:
    _select: str = ""
    _table: str = ""
    _where: str = ""
    # _group: str
    # _order: str
    # _limit: str
    
    def select(self, *args)->GQuery:
        self._select = ', '.join(args)
        return self
    
    def table(self, table: str)->GQuery:
        self._table = table
        return self
    
    def where(self, condition: str)->GQuery:
        self._where = condition
        return self
    
    
    def gquery(self)->str: 
        """
        gquery build the SQLite3 query from the GQuery object.

        Returns:
            str: The SQLite3 query that can be send to any ORM.
        """
        parts = []
        parts.append('SELECT')
        if self._select:
            parts.append(self._select)
        else:
            parts += ['*']
        
        parts.append('FROM')
        parts.append(self._table)
        
        if self._where:
            parts.append('WHERE')
            parts.append(self._where)
        
        return ' '.join(parts)     
            

if __name__ == "__main__":
    q = GQuery().select('name')
    print(q.gquery())