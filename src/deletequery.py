from src.gquery import GQuery


class DeleteQuery(GQuery):
    
    def build_query(self)->str:
        parts = ['DELETE']
        
        if self._table: parts.append(self._table)
        if self._where: parts.append(self._where)
        
        return ' '.join(parts)