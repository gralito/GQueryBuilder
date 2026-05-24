from src.GQueryBuilder.gquery import GQuery


class UpdateQuery(GQuery):
    def __init__(self, database):
        super().__init__(database)
        self._expressions = ""
    
    def expressions(self, expressions: dict):
        result = []
        for key, value in expressions.items():
            if type(value) == str:
                str_value = f"'{value}'"
            else :
                str_value = f"{value}"
            result.append(f"{key} = {str_value}")
        self._expressions = ", ".join(result)
        return self
        
    
    def build_query(self)->str:
        """
        build the SQLite SELECT query using the instance attributes.

        Returns:
            str: the SQLite query, ready to use.
        """
        parts = []
        parts.append("UPDATE")
        parts.append(self._table)
        parts.append("SET")
        parts.append(self._expressions)
        if self._where: parts.append(self._where)
        
        self._build_query(parts)