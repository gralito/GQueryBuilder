import unittest
from src.gquery import GQuery
import utils.dbtools as dbt


class GQueryTest(unittest.TestCase):
    
    def testSimpleAlias(self):
        q = GQuery().table(('posts', 'p'))
        self.assertEqual(str(q._table),
                         'FROM posts as p')
    
    def testSimpleWhereQuery(self):
        q = GQuery().where('a = :a')
        self.assertEqual(q._where,
                         'WHERE a = :a')
        
    def testComplexWhereQuery(self):
        q = GQuery().where(dbt.build_and(dbt.build_or("a = :a", "b = :b"), "c = :c"))
        self.assertEqual(str(q._where),
                         "WHERE ((a = :a OR b = :b) AND c = :c)")
        