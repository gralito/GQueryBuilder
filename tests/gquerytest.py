import unittest
from src.gquery import GQuery
import utils.dbtools as dbt


class GQueryTest(unittest.TestCase):
    
    def testSimpleAlias(self):
        q = GQuery().table(('posts', 'p'))
        query = q.gquery()
        self.assertEqual(str(query),
                         'FROM posts as p')
    
    def testSimpleWhereQuery(self):
        q = GQuery().where('a = :a')
        query = q.gquery()
        self.assertEqual(str(query),
                         'WHERE a = :a')
        
    def testComplexWhereQuery(self):
        q = GQuery().where(dbt.build_and(dbt.build_or("a = :a", "b = :b"), "c = :c"))
        query = q.gquery()
        self.assertEqual(str(query),
                         "WHERE ((a = :a OR b = :b) AND c = :c)")
        