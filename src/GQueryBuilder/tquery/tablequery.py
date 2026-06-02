from src.GQueryBuilder.gquery import GQuery


class TableQuery(GQuery):
    """
    parent class

    Args:
        _name (str): name of the table concerned by the query.
    """
    
    def __init__(self, database: str):
        super().__init__(database=database)
        
    def name(self, name: str):
        """
        set the name of the working table.

        Returns:
            TableQuery: returns the instance, allowing fluent coding.
        """
        self._name = name
        return self