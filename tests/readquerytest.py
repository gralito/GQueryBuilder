import unittest

from src.GQueryBuilder.readquery import ReadQuery


class ReadQueryTest(unittest.TestCase):
    
    def setUp(self):
        self.database = "/home/gralito/repos/GQueryBuilder/tests/test_db.sqlite"
        self.query = ReadQuery(self.database)
    
    def test_simple_select_query(self):
        q = ReadQuery(self.database)
        q.table(('posts',)).select('name').build_query()
        self.assertEqual(q._query,
                         'SELECT name FROM posts')
         
    def test_simple_query_select_several_fields(self):
        q = ReadQuery(self.database)
        q.table(('posts',))
        q.select('name', 'value', 'date').build_query()
        self.assertEqual(q._query,
                         "SELECT name, value, date FROM posts")
        
    def test_simple_query_select_all_fields_calling_method(self):
        q = ReadQuery(self.database)
        q.table(('posts',))
        q.select().build_query()
        self.assertEqual(q._query,
                         'SELECT * FROM posts')
            
    def test_simple_query_select_all_fields(self):
        q = ReadQuery(self.database)
        q.table(('posts',)).build_query()
        self.assertEqual(q._query,
                         'SELECT * FROM posts') 
        
    def test_select_all_fields_with_alias(self):
        q = ReadQuery(self.database)
        q.table(('posts', 'p'), ('blog', 'b')).build_query()
        self.assertEqual(q._query,
                         "SELECT * FROM posts as p, blog as b")
    
    def test_simple_query_with_distinct(self):
        q = ReadQuery(self.database)
        q.select('username', distinct=True)
        q.table(('posts', 'p')).build_query()
        self.assertEqual(q._query,
                         "SELECT DISTINCT username FROM posts as p")

    def test_query_with_group_by(self):
        q = ReadQuery(self.database)
        q.table(('posts',))
        q.options(group='city').build_query()
        self.assertEqual(q._query,
                         "SELECT * FROM posts GROUP BY city")
        
    def test_query_with_order_by(self):
        q = ReadQuery(self.database)
        q.table(('posts',))
        q.options(order='city').build_query()
        self.assertEqual(q._query,
                         "SELECT * FROM posts ORDER BY city")
    
    def test_query_with_limit(self):
        q = ReadQuery(self.database)
        q.table(('posts',))
        q.options(limit=5).build_query()
        self.assertEqual(q._query,
                         "SELECT * FROM posts LIMIT 5")
        
    def test_complex_query(self):
        q = ReadQuery(self.database).table(('posts', 'p'), ('articles',))
        q.select('name', 'age').where("city='NY'")
        q.options(limit=5, order='city').build_query()
        self.assertEqual(q._query,
                         "SELECT name, age FROM posts as p, articles WHERE city='NY' ORDER BY city LIMIT 5")
        
    def test_run_method(self):
        self.query.select('name', 'age').table(('users',))
        self.query.where("city='paris'")
        response = self.query.build_query().run(receive=True)
        
        self.assertEqual(response,
                         [('jacques2', 29), ('pierrot', 19)])