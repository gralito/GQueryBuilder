import utils.dbtools as dbt


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
    
    def table(self, *args: tuple[str, ...])->GQuery:
        result = []
        for arg in args:
            if len(arg) == 1:
                result.append(arg[0])
            else:
                result.append(f"{arg[0]} as {arg[1]}")
        self._table = ", ".join(result)
        print(self._table)
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
        
        ### SELECT ### 
        parts.append('SELECT')
        if self._select:
            parts.append(self._select)
        else:
            parts += ['*']
        
        ### FROM ###
        parts.append('FROM')
        parts.append(self._table)
        
        ### WHERE ###
        if self._where:
            parts.append('WHERE')
            parts.append(self._where)
        
        return ' '.join(parts)     
            

if __name__ == "__main__":
    q = GQuery().table(('posts',), ('blog', 'b'))
    print(q.gquery())