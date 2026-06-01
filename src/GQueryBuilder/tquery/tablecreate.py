from src.GQueryBuilder.tquery.tablequery import TableQuery


class TableCreate(TableQuery):
    
    def __init__(self, database: str, name: str)->TableCreate:
        super().__init__(database=database)
        self._name = name
        self._fields = []
        
    def add_field(self, 
                  name: str,
                  type: str,
                  primary_key: bool = False,
                  auto_increment: bool = False,
                  not_null: bool = False,
                  unique: bool = False,
                  default_value: str = "")->TableCreate:
        field = f"{name} {type}"
        if primary_key: 
            field += ' PRIMARY KEY'
            if auto_increment: field += ' AUTOINCREMENT'
        if not_null: field += ' NOT NULL'
        if unique: field += ' UNIQUE'
        if default_value: field += f' DEFAULT {default_value}'
        self._fields.append(field)
        return self
    
    def _build_fields(self):
        return "(" + ", ".join(self._fields) + ")"
    
    def build_query(self):
        parts = ['CREATE TABLE']
        parts.append(self._name)
        parts.append(self._build_fields())
        self._build_query(parts)
        return self