import unittest
from calc import add, subtruct, multiply, divide

class TestCase(unittest.TestCase):
    def test_add(self):
        result = add(10, 5)
        self.assertEqual(result, 15)

    def test_subtruct(self):
        result  = subtruct(10, 5)
        self.assertEqual(result, 5)

    def test_multiply(self):
        result  = multiply(10, 5)
        self.assertEqual(result, 50)

    
    def test_divide(self):
        result  = divide(10, 5)
        self.assertEqual(result, 2.0)


if __name__ == "__main__":
    unittest.main()
