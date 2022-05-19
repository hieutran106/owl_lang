import unittest
from src.scanner import Scanner

class TestScanner(unittest.TestCase):
    def test_case1(self):
        scanner = Scanner("+-*/")
        self.assertEqual(1, 2)


if __name__ == "__main__":
    unittest.main()