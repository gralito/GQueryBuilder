import unittest

from src.GQueryBuilder.gquery import GQuery
import src.GQueryBuilder.utils.dbtools as dbt


class GQueryTest(unittest.TestCase):
    def setUp(self):
        self.database = "db.sqlite3"
    
    def test_simple_alias(self):
        q = GQuery(self.database).table(('posts', 'p'))
        self.assertEqual(str(q._table),
                         'posts as p')
    
    def test_simple_where(self):
        q = GQuery(self.database).where('a = :a')
        self.assertEqual(q._where,
                         'WHERE a = :a')
        
    def test_complex_where(self):
        q = GQuery(self.database).where(dbt.and_(dbt.or_("a = :a", "b = :b"), "c = :c"))
        self.assertEqual(str(q._where),
                         "WHERE ((a = :a OR b = :b) AND c = :c)")
        
    def test_set_database(self):
        q = GQuery(self.database)
        self.assertEqual(q.database, "db.sqlite3")