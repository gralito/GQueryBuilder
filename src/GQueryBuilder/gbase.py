


class GBase:
    def __init__(self, path: str, name: str = ""):
        self.path = path
        self.name = self.set_auto_db_name() if name == "" else name
            
            
    def set_auto_db_name(self):
        return "-".join(self.path.split('/')[-1].split('.')[:-1])
        
    ### TABLES ###
    def add_table(self):
        pass
    
    def remove_table(self):
        pass
    
    def update_table(self):
        pass
    
    
    ### ENTRIES ###
    def get_entries(self):
        pass
    
    def get_entry(self):
        pass
    
    def add_entry(self):
        pass
    
    def remove_entry(self):
        pass
    
    def update_entry(self):
        pass

if __name__ == '__main__':
    db1 = GBase("/home/gralito/repos/GQueryBuilder/tests/test_db.sqlite")
    db2 = GBase("/home/gralito/repos/GQueryBuilder/tests/test_db.sqlite", "dbase")
    
    print(db1.name)
    print(db2.name)