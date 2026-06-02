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
    
    def test_add_fields_with_options(self):
        q = TableCreate(self.database, 'users')
        q.add_field('username', 'TEXT', not_null=True,unique=True)
        q.add_field('age', 'INTEGER', not_null=True,default_value='18')
        q.build_query()
        
        self.assertEqual(q._query,
                         "CREATE TABLE users (username TEXT NOT NULL UNIQUE, age INTEGER NOT NULL DEFAULT 18)")