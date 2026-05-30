import unittest

from src.GQueryBuilder.utils.dbase import run


class DBaseTest(unittest.TestCase):
    def test_run(self):
        database = "/home/gralito/repos/GQueryBuilder/tests/test_db.sqlite"
        query = "SELECT name FROM users WHERE city='saintois'"
        response = run(database=database,
            query=query,
            receive=True)
        
        self.assertEqual(response,
                         [('gralito',), ('mimi',), ('touti',)])