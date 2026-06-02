import unittest

from src.GQueryBuilder.equery.entryupdate import EntryUpdate


class EntryUpdateTest(unittest.TestCase):
    
    def setUp(self):
        self.database = "/home/gralito/repos/GQueryBuilder/tests/test_db.sqlite"
        self.query = EntryUpdate(self.database)
        
    def test_simple_query(self):
        self.query.table(('posts',))
        changes = {'name': 'gralito'}
        self.query.expressions(changes)
        self.query.build_query()
        self.assertEqual(self.query._query,
                         "UPDATE posts SET name='gralito'")
        
    def test_simple_where_query(self):
        self.query.table(('posts', 'p'))
        changes = {'name': 'gralito'}
        self.query.expressions(changes)
        self.query.where("id=12")
        self.query.build_query()
        self.assertEqual(self.query._query,
                         "UPDATE posts as p SET name='gralito' WHERE id=12")
    
    def test_complex_query(self):
        self.query.table(('posts', 'p'))
        changes = {
            'name': 'julien',
            'age': 43
        }
        self.query.expressions(changes)
        self.query.where('id=12')
        self.query.build_query()
        self.assertEqual(self.query._query,
                         "UPDATE posts as p SET name='julien', age=43 WHERE id=12")