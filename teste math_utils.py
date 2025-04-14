import unittest
from math_utils import add, subtract

class TestMathUtils(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(4,6),10)
        self.assertEqual(add(-2,2),0)

    def test_subtract(self):
        self.assertEqual(add(10,5),5)
        self.assertEqual(add(0,0),0)

if __name__ == '__main__':
    unittest.main()
