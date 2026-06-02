from src.GQueryBuilder.tquery.tablequery import TableQuery


class TableCreate(TableQuery):
    """
    this class represents a `CREATE TABLE` query.

    Attributes:
        _name (str): the name of the created table.
        _fields ([str]): an array of the fields inserted in the table.
    """
    
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
        """
        create a new field and add it to the `_fields` array.

        Args:
            name (str): name of the field.
            type (str): data type of the field, can be either `TEXT` `INT` `NUM` `REAL` or `""`(BLOB)
            primary_key (bool, optional): determine if the field is a `PRIMARY KEY`. Defaults to False.
            auto_increment (bool, optional): determine if the field is auto-incremental. Defaults to False.
            not_null (bool, optional): determine if the field can have a `NULL` value. Defaults to False.
            unique (bool, optional): determine if each field data has to be unique. Defaults to False.
            default_value (any, optional): gives a default value to the field. Defaults to "".

        Returns:
            TableCreate: returns the instance, allowing fluent coding.
        """
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
        """
        build the 'field' part of the query, using the `self._fields` attribute.

        Returns:
            str: the fields definition part of the query.
        """
        return "(" + ", ".join(self._fields) + ")"
    
    def build_query(self):
        """
        build the SQLite query from the TableCreate object.

        Returns:
            TableCreate: return the instance, allowing fluent coding.
        """
        parts = ['CREATE TABLE']
        
        parts.append(self._name)
        parts.append(self._build_fields())
        
        self._build_query(parts)
        return self