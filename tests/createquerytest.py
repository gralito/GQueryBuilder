import unittest

from src.GQueryBuilder.createquery import CreateQuery
from src.GQueryBuilder.gquery import GQuery


class CreateQueryTest(unittest.TestCase):
    
    def setUp(self):
        self.database = "/home/gralito/repos/GQueryBuilder/tests/test_db.sqlite"
        self.query = CreateQuery(self.database)
    
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
        
    def test_run_method(self):
        self.query.table(('users',))
        self.query.target(['name', 'age', 'city'])
        self.query.values(['touti', 6, 'saintois'])
        self.query.build_query().run()
        
        check = GQuery(self.database)
        check._query = "SELECT DISTINCT age, city FROM users WHERE name='touti'"
        check_response = check.run(receive=True)
        
        self.assertEqual(check_response,
                         [(6, 'saintois')])
        