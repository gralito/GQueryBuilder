import unittest

from src.GQueryBuilder.gquery import GQuery


class GQueryTest(unittest.TestCase):
    def setUp(self):
        self.database = "/home/gralito/repos/GQueryBuilder/tests/test_db.sqlite"
    
    def test_run_method(self):
        q = GQuery(self.database)
        q._query = "SELECT name FROM users WHERE id=12"
        response = q.run(True)
        self.assertEqual(response,
                         [('gralito',)])
        
    def test_build_query(self):
        q = GQuery(self.database)
        parts = ["SELECT *", "FROM users as u"]
        q._build_query(parts)
        self.assertEqual(q._query,
                         "SELECT * FROM users as u")