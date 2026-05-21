import utils.dbtools as dbt


class GQuery:
    _table: str = ""
    _where: str = ""
    # _group: str
    # _order: str
    # _limit: str
    
    def table(self, *args: tuple[str, ...])->GQuery:
        """
        table: set the working table.

        Returns:
            GQuery: returns the instance.
        """
        result = []
        for arg in args:
            if len(arg) == 1:
                result.append(arg[0])
            else:
                result.append(f"{arg[0]} as {arg[1]}")
        self._table = "FROM " + ", ".join(result)
        return self
    
    def where(self, condition: str)->GQuery:
        self._where = "WHERE " + condition
        return self
    
    def gquery(self)->str: 
        """
        gquery: build the SQLite3 query from the GQuery object.

        Returns:
            str: The SQLite3 query that can be send to any ORM.
        """
        parts = []
        
        # ### SELECT ### 
        # if self._select:
        #     parts.append(self._select)
        
        # ### FROM ###
        # if self._table:
        #     parts.append('FROM')
        #     parts.append(self._table)
        
        # ### WHERE ###
        # if self._where:
        #     parts.append('WHERE')
        #     parts.append(self._where)
        
        # return ' '.join(parts)     
            

if __name__ == "__main__":
    pass