import unittest

from src.GQueryBuilder.createquery import CreateQuery


class CreateQueryTest(unittest.TestCase):
    
    def setUp(self):
        self.query = CreateQuery('db.sqlite3')
    
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