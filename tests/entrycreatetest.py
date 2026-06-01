import unittest

from src.GQueryBuilder.equery.entrycreate import EntryCreate


class EntryCreateTest(unittest.TestCase):
    def setUp(self):
        self.database = "/home/gralito/repos/GQueryBuilder/tests/test_db.sqlite"
        self.query = EntryCreate(self.database)
    
    def test_simple_query(self):
        self.query.table(('posts',))
        self.query.target(['name']).values(['julien'])
        self.query.build_query()
        self.assertEqual(self.query._query,
                         "INSERT INTO posts (name) VALUES ('julien')")
        
    def test_multiple_values(self):
        self.query.table(('posts', 'p'))
        self.query.target(['name', 'age'])
        self.query.values(['julien', 43])
        self.query.build_query()
        self.assertEqual(self.query._query,
                         "INSERT INTO posts as p (name, age) VALUES ('julien', 43)")
    
    def test_default_values(self):
        self.query.table(('posts',))
        self.query.target(['name'])
        self.query.build_query()
        self.assertEqual(self.query._query,
                         "INSERT INTO posts (name) DEFAULT VALUES")