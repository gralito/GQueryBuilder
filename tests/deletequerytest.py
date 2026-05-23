import unittest

from src.GQueryBuilder.deletequery import DeleteQuery


class DeleteQueryTest(unittest.TestCase):
    def test_simple_delete_query(self):
        q = DeleteQuery()
        q.table(('posts',))
        query = q.build_query()
        self.assertEqual(str(query),
                         "DELETE FROM posts")
    
    def test_delete_query_with_where(self):
        q = DeleteQuery().table(('posts',))
        q.where("name='sarah'")
        query = q.build_query()
        self.assertEqual(str(query),
                         "DELETE FROM posts WHERE name='sarah'")
    
    def test_delete_query_with_where_and_alias(self):
        q = DeleteQuery().table(('posts', 'p'))
        q.where("name='ju'")
        query = q.build_query()
        self.assertEqual(str(query),
                         "DELETE FROM posts as p WHERE name='ju'")