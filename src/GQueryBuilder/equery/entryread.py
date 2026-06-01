from src.GQueryBuilder.equery.entryquery import EntryQuery


class EntryRead(EntryQuery):
    """
    this class represents a `SELECT` query.
    
    Attributes:
        _select (str): the SELECT component of the query (`SELECT *` by default)
        _options (dict): the query's options (  
            `group=<field>` -> GROUP BY  
            `order=<field>` -> ORDER BY  
            `limit=<int>` -> LIMIT )
        """

    def __init__(self, database):
        super().__init__(database)
        self._select: str = "SELECT *"
        self._options: dict = {}
    
    def select(self, *args, distinct:bool=False)->EntryRead:
        """
        define the fields name in the SELECT query.
        if no argument is provided or if the method is not called, it will be a 'SELECT *' query.

        Args:
            *args (str): the queried fields.
            distinct (bool, optional): add a DISTINCT option to the query (set to False by default).
        Returns:
            EntryRead:  return the instance, allowing fluent coding.
        """
        option = ""
        if distinct : option = "DISTINCT "
        if args != ():
            self._select = 'SELECT ' + option + ', '.join(args)
        return self
    
    def options(self, **kwargs)->EntryRead:
        """
        define the GROUP BY, ORDER BY and LIMIT options of the query. 
        
        Args:
            group (str, optional): the GROUP BY expression,
            order (str, optional): the ORDER BY expression,
            limit (int, optional): the value of LIMIT integer.         

        Returns:
            EntryRead: return the instance, allowing fluent coding.
        """
        
        if 'group' in kwargs: self._options['group'] = kwargs['group']
        if 'order' in kwargs: self._options['order'] = kwargs['order']
        if 'limit' in kwargs: self._options['limit'] = kwargs['limit']
        
        return self
        
    def _build_options(self)->str:
        """
        build the options part of the SELECT query (ORDER BY, GROUP BY, LIMIT). this private method is called inside the build_query() method.

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
    
    def build_query(self)->EntryRead:
        """
        build the SQLite Squery from the ReadQuery object.

        Returns:
            EntryRead: return instance, allowing fluent coding.
        """
        parts = []
                
        parts.append(self._select)
        if self._table: parts.append(f"FROM {self._table}")
        if self._where: parts.append(self._where)
        if self._options != {}:
            options = self._build_options()
            parts.append(options)
            self._options = {}       
        self._build_query(parts)
        
        return self