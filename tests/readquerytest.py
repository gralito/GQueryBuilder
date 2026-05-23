import unittest

from src.GQueryBuilder.readquery import ReadQuery


class ReadQueryTest(unittest.TestCase):
    
    def test_simple_select_query(self):
        q = ReadQuery()
        q.table(('posts',)).select('name')
        query = q.build_query()
        self.assertEqual(str(query),
                         'SELECT name FROM posts')
         
    def test_simple_query_select_several_fields(self):
        q = ReadQuery()
        q.table(('posts',))
        q.select('name', 'value', 'date')
        query = q.build_query()
        self.assertEqual(str(query),
                         "SELECT name, value, date FROM posts")
        
    def test_simple_query_select_all_fields_calling_method(self):
        q = ReadQuery()
        q.table(('posts',))
        q.select()
        query = q.build_query()
        self.assertEqual(str(query),
                         'SELECT * FROM posts')
            
    def test_simple_query_select_all_fields(self):
        q = ReadQuery()
        q.table(('posts',))
        query = q.build_query()
        self.assertEqual(str(query),
                         'SELECT * FROM posts') 
        
    def test_select_all_fields_with_alias(self):
        q = ReadQuery()
        q.table(('posts', 'p'), ('blog', 'b'))
        query = q.build_query()
        self.assertEqual(str(query),
                         "SELECT * FROM posts as p, blog as b")
    
    def test_simple_query_with_distinct(self):
        q = ReadQuery()
        q.select('username', distinct=True)
        q.table(('posts', 'p'))
        query = q.build_query()
        self.assertEqual(str(query),
                         "SELECT DISTINCT username FROM posts as p")

    def test_query_with_group_by(self):
        q = ReadQuery()
        q.table(('posts',))
        q.options(group='city')
        query = q.build_query()
        self.assertEqual(str(query),
                         "SELECT * FROM posts GROUP BY city")
        
    def test_query_with_order_by(self):
        q = ReadQuery()
        q.table(('posts',))
        q.options(order='city')
        query = q.build_query()
        self.assertEqual(str(query),
                         "SELECT * FROM posts ORDER BY city")
    
    def test_query_with_limit(self):
        q = ReadQuery()
        q.table(('posts',))
        q.options(limit=5)
        query = q.build_query()
        self.assertEqual(str(query),
                         "SELECT * FROM posts LIMIT 5")
        
    def test_complex_query(self):
        q = ReadQuery().table(('posts', 'p'), ('articles',))
        q.select('name', 'age').where("city='NY'")
        q.options(limit=5, order='city')
        query = q.build_query()
        self.assertEqual(str(query),
                         "SELECT name, age FROM posts as p, articles WHERE city='NY' ORDER BY city LIMIT 5")