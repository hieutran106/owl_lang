from __future__ import annotations
import unittest
from src.scanner import Scanner
from src.parser import Parser
from rich import print
from src.token_type import TokenType


class TestParser(unittest.TestCase):
    def test_case1(self):
        source = """
                3 + 4 * 3
                """
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()
        parser = Parser(tokens)
        expr = parser.parse()
        self.assertEqual(expr.left.value, 3)
        self.assertEqual(expr.operator.type, TokenType.PLUS)

    def test_case2(self):
        source = """
                3 +
                """
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()
        parser = Parser(tokens)
        expr = parser.parse()


if __name__ == "__main__":
    unittest.main()
