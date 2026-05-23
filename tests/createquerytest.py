import unittest

from src.GQueryBuilder.createquery import CreateQuery


class CreateQueryTest(unittest.TestCase):
    
    def setUp(self):
        self.database = 'db.sqlite3'
    
    def test_simple_query(self):
        q = CreateQuery(self.database).table(('posts',))
        q.target(['name']).values(['julien'])
        q.build_query()
        self.assertEqual(q._query,
                         "INSERT INTO posts (name) VALUES ('julien')")
        
    def test_multiple_values(self):
        q = CreateQuery(self.database)
        q.table(('posts', 'p'))
        q.target(['name', 'age'])
        q.values(['julien', 43])
        q.build_query()
        self.assertEqual(q._query,
                         "INSERT INTO posts as p (name, age) VALUES ('julien', 43)")
    
    def test_default_values(self):
        q = CreateQuery(self.database)
        q.table(('posts',))
        q.target(['name'])
        q.build_query()
        self.assertEqual(q._query,
                         "INSERT INTO posts (name) DEFAULT VALUES")