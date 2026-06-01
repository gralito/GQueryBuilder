import unittest

from src.GQueryBuilder.tquery.tableremove import TableRemove


class TableRemoveTest(unittest.TestCase):
    def setUp(self):
        self.database = "/home/gralito/repos/GQueryBuilder/tests/test_db.sqlite"
        
    def test_simple_remove(self):
        q = TableRemove(self.database)
        q.name('users')
        q.build_query()
        self.assertEqual(q._query,
                         'DROP TABLE users')
        
    def test_if_exists_remove(self):
        q = TableRemove(self.database,
                        if_exists=True)
        q.name('users')
        q.build_query()
        self.assertEqual(q._query,
                         'DROP TABLE IF EXISTS users')