from src.GQueryBuilder.gquery import GQuery


class CreateQuery(GQuery):
    """
    this class represents an`INSERT INTO` query.

    Attributes:
        _target (str): the fields names, separated by a comma.
        _values (str): the values to insert in the table, also separated by a comma.
    """
    def __init__(self, database):
        super().__init__(database)
        self._target = ""
        self._values = ""
    
    def target(self, columns: [str])->CreateQuery:
        """
        define the fields concerned by the `INSERT INTO` query.  
        those fields, separated by a comma, are stored in the `_target` attribute.

        Args:
            columns ([str]): an array containing the fields names.

        Returns:
            CreateQuery: return the instance, allowing fluent coding.
        """
        self._target = f"({", ".join(columns)})"
        return self
            
    def values(self, values: [])->CreateQuery:
        """
        define the values to give to the new entry.  
        Those values are stored in the `_values` attribute.

        Args:
            values (Array): the values are provided as an array containing them.

        Returns:
            CreateQuery: return the instance, allowing fluent coding.
        """
        for element in values:
            if type(element) == str:
                values[values.index(element)] = f"\'{element}\'"
            else:
                values[values.index(element)] = str(element)
        self._values = f"VALUES ({", ".join(values)})"
        return self
    
    def build_query(self)->CreateQuery:
        """
        build the SQLite query from the CreateQuery object.

        Returns:
            CreateQuery: return the instance, allowing fluent coding.
        """
        parts = ["INSERT INTO"]
        parts.append(self._table)
        parts.append(self._target)
        if self._values:
            parts.append(self._values)
        else:
            parts.append("DEFAULT VALUES")
        
        self._build_query(parts)
        return self