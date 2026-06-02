import unittest

from src.GQueryBuilder.equery.entryquery import EntryQuery


class EntryQueryTest(unittest.TestCase):
    def setUp(self):
        self.database = "/home/gralito/repos/GQueryBuilder/tests/test_db.sqlite"
        
    def test_simple_alias(self):
        q = EntryQuery(self.database).table(('posts', 'p'))
        self.assertEqual(str(q._table),
                         'posts as p')
    
    def test_simple_where(self):
        q = EntryQuery(self.database).where('a = :a')
        self.assertEqual(q._where,
                         'WHERE a = :a')
        
    def test_complex_where(self):
        q = EntryQuery(self.database).where("((a = :a OR b = :b) AND c = :c)")
        self.assertEqual(str(q._where),
                         "WHERE ((a = :a OR b = :b) AND c = :c)")