import unittest
from gquery import GQuery
import utils.dbtools as dbt


class GQueryTest(unittest.TestCase):
    def testSimpleQuery(self):
        q = GQuery().table(('posts',)).select('name')
        query = q.gquery()
        self.assertEqual(str(query),
                         'SELECT name FROM posts')
        
    def testSimpleQuerySelectSeveralFields(self):
        q = GQuery().table(('posts',)).select('name', 'value', 'date')
        query = q.gquery()
        self.assertEqual(str(query),
                         "SELECT name, value, date FROM posts")
    
    def testSimpleQuerySelectAll(self):
        q = GQuery().table(('posts',))
        query = q.gquery()
        self.assertEqual(str(query),
                         'SELECT * FROM posts')
    
    def testSimpleQueryAlias(self):
        q = GQuery().table(('posts', 'p')).select('name')
        query = q.gquery()
        self.assertEqual(str(query),
                          'SELECT name FROM posts as p')
    
    def testSimpleWhereQuery(self):
        q = GQuery().select('name').table(('posts',))
        q.where('a = :a')
        query = q.gquery()
        self.assertEqual(str(query),
                         'SELECT name FROM posts WHERE a = :a')
        
    def testComplexWhereQuery(self):
        q = GQuery().select().table(('posts', 'p'))
        q.where(dbt.build_and(dbt.build_or("a = :a", "b = :b"), "c = :c"))
        query = q.gquery()
        self.assertEqual(str(query),
                         "SELECT * FROM posts as p WHERE ((a = :a OR b = :b) AND c = :c)")
        