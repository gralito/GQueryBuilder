import unittest

from src.GQueryBuilder.updatequery import UpdateQuery


class UpdateQueryTest(unittest.TestCase):
    
    def setUp(self):
        self.database = "db.sqlite3"
        
    def test_simple_query(self):
        q = UpdateQuery(self.database)
        q.table(('posts',))
        changes = {'name': 'gralito'}
        q.expressions(changes)
        q.build_query()
        self.assertEqual(q._query,
                         "UPDATE posts SET name = 'gralito'")