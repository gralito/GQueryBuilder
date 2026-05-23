from src.GQueryBuilder.gquery import GQuery


class CreateQuery(GQuery):
    def __init__(self, database):
        self.database = database
        self._values = ""
        self._target = ""
    
    def target(self, columns: [str]):
        self._target = f"({", ".join(columns)})"
        return self
            
    def values(self, values: []):
        for element in values:
            if type(element) == str:
                values[values.index(element)] = f"\'{element}\'"
            else:
                values[values.index(element)] = str(element)
        self._values = f"VALUES ({", ".join(values)})"
        return self
    
    def build_query(self):
        parts = ["INSERT INTO"]
        parts.append(self._table)
        parts.append(self._target)
        if self._values:
            parts.append(self._values)
        else:
            parts.append("DEFAULT VALUES")
        
        self._build_query(parts)
             