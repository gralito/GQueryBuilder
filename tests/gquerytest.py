import unittest
from gquery import GQuery


class GQueryTest(unittest.TestCase):
    def testSimpleQuery(self):
        q = GQuery().table('posts').select('name')
        query = q.gquery()
        self.assertEqual(str(query),
                          'SELECT name FROM posts')
        
    def testSimpleQuerySelectSeveralFields(self):
        q = GQuery().table('posts').select('name', 'value', 'date')
        query = q.gquery()
        self.assertEqual(str(query),
                         "SELECT name, value, date FROM posts")
    
    def testSimpleQuerySelectAll(self):
        q = GQuery().table('posts')
        query = q.gquery()
        self.assertEqual(str(query),
                         'SELECT * FROM posts')
        
    def testSelectWhereQuery(self):
        q = GQuery().select('name').table('posts').where('category = livre')
        query = q.gquery()
        self.assertEqual(str(query),
                         'SELECT name FROM posts WHERE category = livre')