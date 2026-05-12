import unittest

import utils.dbtools as dbt

class DbtoolsTest(unittest.TestCase):
    def testOr(self):
        a = "A"
        b = "B"
        self.assertEqual(dbt.build_or(a, b), '(A OR B)')

    def testAnd(self):
        a = "A"
        b = "B"
        self.assertEqual(dbt.build_and(a, b), '(A AND B)')