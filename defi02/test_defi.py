import unittest
from defi import upperFirstLetter, optimizedFirstLetter


class TestDefi(unittest.TestCase):
    def test_upperFirstLetter(self):
        self.assertEqual(upperFirstLetter("hello world"), "Hello World")

    def test_optimizedFirstLetter(self):
        self.assertEqual(optimizedFirstLetter("hello world"), "Hello World")

if __name__ == '__main__':
    unittest.main()