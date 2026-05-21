import unittest
from src.gquery import GQuery
import utils.dbtools as dbt


class GQueryTest(unittest.TestCase):
    
    def test_simple_alias(self):
        q = GQuery().table(('posts', 'p'))
        self.assertEqual(str(q._table),
                         'FROM posts as p')
    
    def test_simple_where(self):
        q = GQuery().where('a = :a')
        self.assertEqual(q._where,
                         'WHERE a = :a')
        
    def test_complex_where(self):
        q = GQuery().where(dbt.build_and(dbt.build_or("a = :a", "b = :b"), "c = :c"))
        self.assertEqual(str(q._where),
                         "WHERE ((a = :a OR b = :b) AND c = :c)")
        
     