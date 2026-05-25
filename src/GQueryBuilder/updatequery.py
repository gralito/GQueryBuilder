from src.GQueryBuilder.gquery import GQuery


class UpdateQuery(GQuery):
    """
    this class represents a `UPDATE` query

    Attributes:
        _expressions (str): the modifications to bring to the table, the SET part of the query.
    """
    def __init__(self, database):
        super().__init__(database)
        self._expressions = ""
    
    def expressions(self, expressions: dict):
        """
        define the modifications to bring to the table.

        Args:
            expressions (dict): a dictionnary where each key is the field to modify and the value is the new value.

        Returns:
            UpdateQuery: return the instance, allowing fluent coding.
        """
        result = []
        for key, value in expressions.items():
            if type(value) == str:
                str_value = f"'{value}'"
            else :
                str_value = f"{value}"
            result.append(f"{key}={str_value}")
        self._expressions = ", ".join(result)
        return self
         
    def build_query(self)->str:
        """
        build the SQLite query from the UpdateQuery object.

        Returns:
            UpdateQuery: return the instance, allowing fluent coding.
        """
        parts = []
        parts.append("UPDATE")
        parts.append(self._table)
        parts.append("SET")
        parts.append(self._expressions)
        if self._where: parts.append(self._where)
        
        self._build_query(parts)
        return self