from src.gquery import GQuery


class ReadQuery(GQuery):
    """class used to generate a 'SELECT' query"""

    def __init__(self):
        self._select: str = "SELECT *"
        self._options: dict = {}
    
    def select(self, *args, distinct:bool=False)->ReadQuery:
        """
        define the fields name in the SELECT query.
        if no argument is precised or if the method is
        not called, it will be a 'SELECT *' query.
        Args:
            *args (str): the queried fields.
            distinct (bool, optional): add a DISTINCT option to the query.
        Returns:
            ReadQuery:  the instance is returned.
                        it allows a fluent behavior.
        """
        option = ""
        if distinct : option = "DISTINCT "
        if args != ():
            self._select = 'SELECT ' + option + ', '.join(args)
        return self
    
    def options(self, **kwargs):
        """
        define the GROUP BY, ORDER BY and LIMIT options of the query. 
        Args:
            group (str, optional): the GROUP BY expression,
            order (str, optional): the ORDER BY expression,
            limit (int, optional): the value of LIMIT integer.         
        Returns:
            ReadQuery: returns the instance
        """
        
        if 'group' in kwargs: self._options['group'] = kwargs['group']
        if 'order' in kwargs: self._options['order'] = kwargs['order']
        if 'limit' in kwargs: self._options['limit'] = kwargs['limit']
        
        return self
        
    def _build_options(self)->str:
        """
        build the options part of the SELECT query (ORDER BY, GROUP BY, LIMIT)

        Returns:
            str: the option string, ready to inject in the query
        """
        
        parts = []
        
        if 'group' in self._options:
            parts.append(f"GROUP BY {self._options['group']}")
        if 'order' in self._options:
            parts.append(f"ORDER BY {self._options['order']}")
        if 'limit' in self._options:
            parts.append(f"LIMIT {self._options['limit']}")
            
        return " ".join(parts)
    
    def build_query(self)->str:
        """
        build the SQLite SELECT query using the instance attributes.

        Returns:
            str: the SQLite query, ready to use.
        """
        parts = []
                
        parts.append(self._select)
        if self._table: parts.append(self._table)
        if self._where: parts.append(self._where)
        if self._options != {}:
            options = self._build_options()
            parts.append(options)
            self._options = {}
               
        return self._build_query(parts)
   