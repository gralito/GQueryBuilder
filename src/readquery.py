from src.gquery import GQuery


class ReadQuery(GQuery):
    _select: str = "SELECT *"
    
    def select(self, *args)->ReadQuery:
        """
        define the fields name in the SELECT query.
        if no argument is precised or if the method is
        not called, it will be a 'SELECT *' query.

        Returns:
            ReadQuery:  the instance is returned.
                        it allows a fluent behavior.
        """
        if args != ():
            self._select = 'SELECT ' + ', '.join(args)
        return self
    
    def build_query(self):
        parts = []
        
        parts.append(self._select)
        if self._table: parts.append(self._table)
        if self._where: parts.append(self._where)
        
        return ' '.join(parts)