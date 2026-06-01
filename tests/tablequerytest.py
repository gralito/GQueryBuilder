import unittest

from src.GQueryBuilder.tquery.tablequery import TableQuery


class TableQueryTest(unittest.TestCase):
    def setUp(self):
        self.database = "/home/gralito/repos/GQueryBuilder/tests/test_db.sqlite"
    
    def test_method_name(self):
        q = TableQuery(self.database)
        q.name('users')
        self.assertEqual(q._name,
                         'users')