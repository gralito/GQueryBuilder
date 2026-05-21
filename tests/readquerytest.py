import unittest
from src.readquery import ReadQuery


class ReadQueryTest(unittest.TestCase):
    
    def test_simple_select_query(self):
        q = ReadQuery()
        q.table(('posts',)).select('name')
        query = q.build_query()
        self.assertEqual(str(query),
                         'SELECT name FROM posts')
         
    def test_simple_query_select_several_fields(self):
        q = ReadQuery().table(('posts',))
        q.select('name', 'value', 'date')
        query = q.build_query()
        self.assertEqual(str(query),
                         "SELECT name, value, date FROM posts")
        
    def test_simple_suery_select_all_fields_calling_method(self):
        q = ReadQuery().table(('posts',))
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
    
<<<<<<< HEAD
    def test_simple_query_with_distinct(self):
        q = ReadQuery().select('username', distinct=True)
        q.table(('posts', 'p'))
        query = q.build_query()
        self.assertEqual(str(query),
                         "SELECT DISTINCT username FROM posts as p")
=======
    
>>>>>>> feature/ReadQuery
