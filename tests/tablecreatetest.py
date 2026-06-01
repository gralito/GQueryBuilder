import unittest

from src.GQueryBuilder.tquery.tablecreate import TableCreate


class TableCreateTest(unittest.TestCase):
    def setUp(self):
        self.database = "/home/gralito/repos/GQueryBuilder/tests/test_db.sqlite"
        
    def test_add_simple_field(self):
        q = TableCreate(self.database, 'users')
        q.add_field('username', 'TEXT')
        q.build_query()
        self.assertEqual(q._query,
                         'CREATE TABLE users (username TEXT)')
        
    def test_add_two_simple_fields(self):
        q = TableCreate(self.database, 'users')
        q.add_field('username', 'TEXT').add_field('age', 'INTEGER')
        q.build_query()
        self.assertEqual(q._query,
                         'CREATE TABLE users (username TEXT, age INTEGER)')