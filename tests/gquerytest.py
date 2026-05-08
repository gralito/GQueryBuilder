import unittest
from gquery import GQuery


class GQueryTest(unittest.TestCase):
    def testSimpleQuery(self):
        q = GQuery().from_table('posts').select('name')
        query = q.gquery()
        self.assertEqual(str(query),
                          'SELECT name FROM posts')
        
    def testSimpleQuerySelectSeveral(self):
        q = GQuery().from_table('posts').select('name', 'value', 'date')
        query = q.gquery()
        self.assertEqual(str(query),
                         "SELECT name, value, date FROM posts")
    
    def testSimpleQuerySelectAll(self):
        q = GQuery().from_table('posts')
        query = q.gquery()
        self.assertEqual(str(query),
                         'SELECT * FROM posts')