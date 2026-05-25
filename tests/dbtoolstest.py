import unittest

import src.GQueryBuilder.utils.dbtools as dbt

class DbtoolsTest(unittest.TestCase):
    def testOr(self):
        a = "A"
        b = "B"
        self.assertEqual(dbt.or_(a, b), '(A OR B)')

    def testAnd(self):
        a = "A"
        b = "B"
        self.assertEqual(dbt.and_(a, b), '(A AND B)')