import unittest

from src.GQueryBuilder.deletequery import DeleteQuery


class DeleteQueryTest(unittest.TestCase):
    
    def setUp(self):
        self.database = 'db.sqlite3'
    
    def test_simple_delete_query(self):
        q = DeleteQuery(self.database)
        q.table(('posts',)).build_query()
        self.assertEqual(q._query,
                         "DELETE FROM posts")
    
    def test_delete_query_with_where(self):
        q = DeleteQuery(self.database).table(('posts',))
        q.where("name='sarah'").build_query()
        self.assertEqual(q._query,
                         "DELETE FROM posts WHERE name='sarah'")
    
    def test_delete_query_with_where_and_alias(self):
        q = DeleteQuery(self.database).table(('posts', 'p'))
        q.where("name='ju'").build_query()
        self.assertEqual(q._query,
                         "DELETE FROM posts as p WHERE name='ju'")