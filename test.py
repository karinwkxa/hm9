import unittest
from main import *

class My_Test(unittest.TestCase):

    def test_args(self):
        result, t = adder(5, 9)
        self.assertEqual(result, 14)

    def test_args2(self):
        result, t = adder(16,78,340,89)
        self.assertEqual(result, 523)

    def test_kwargs(self):
        result, t = adder(a=1899877, b=18778881)
        self.assertEqual(result, 20678758)


if __name__ == "__main__":
    unittest.main()