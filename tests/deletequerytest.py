import unittest

from src.GQueryBuilder.deletequery import DeleteQuery
from src.GQueryBuilder.gquery import GQuery


class DeleteQueryTest(unittest.TestCase):
    
    def setUp(self):
        self.database = "/home/gralito/repos/GQueryBuilder/tests/test_db.sqlite"
        self.query = DeleteQuery(self.database)
    
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
        
    def test_run_method(self):
        pre_req = GQuery(self.database)
        pre_req._query = "INSERT INTO users ('name', 'age', 'city') VALUES ('souris', 3, 'saintois')"
        pre_req.run()
        
        q = DeleteQuery(self.database)
        q.table(('users',)).where("name='souris'")
        q.build_query().run()
        
        post_req = GQuery(self.database)
        post_req._query = "SELECT * FROM users WHERE name='souris'"
        repsonse = post_req.run(True)
        
        self.assertEqual(repsonse, [])