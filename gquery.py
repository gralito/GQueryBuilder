


class GQuery:
    parts = []
    _select = []
    _from_table: str
    _where = []
    _group = []
    _order: str
    _limit: str
    
    def from_table(self, table: str)->GQuery:
        self._from_table = table
        return self
    
    def select(self, *args)->GQuery:
        self._select = ', '.join(args)
        return self
        
    def gquery(self)->str: 
        self.parts = ['SELECT']
        if self._select:
            self.parts.append(self._select)
        else:
            self.parts += ['*']
        
        self.parts.append('FROM')
        self.parts.append(self._from_table)
        return ' '.join(self.parts)     
            

if __name__ == "__main__":
    q = GQuery().select('name')
    print(q.gquery())