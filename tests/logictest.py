import unittest

from src.GQueryBuilder.utils.logic import and_
from src.GQueryBuilder.utils.logic import or_

class LogicTest(unittest.TestCase):
    def testOr(self):
        a = "A"
        b = "B"
        self.assertEqual(or_(a, b), '(A OR B)')

    def testAnd(self):
        a = "A"
        b = "B"
        self.assertEqual(and_(a, b), '(A AND B)')