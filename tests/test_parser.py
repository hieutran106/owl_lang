from __future__ import annotations
import unittest
from src.scanner import Scanner
from src.parser import Parser
from src.token_type import TokenType


class TestParser(unittest.TestCase):
    def test_case1(self):
        source = """
                3 + 4 * 3
                """
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()
        parser = Parser(tokens)
        expr = parser.expression()
        self.assertEqual(expr.left.value, 3)
        self.assertEqual(expr.operator.type, TokenType.PLUS)

    def test_error_expect_expression(self):
        source = """
                3 +
                """
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()
        parser = Parser(tokens)
        expr = parser.expression()
        self.assertEqual(parser.parse_errors[0].message, "Expect expression.")
        self.assertEqual(parser.parse_errors[0].token.type, TokenType.EOF)

    def test_error_grouping(self):
        source = """
                (3+4
                """
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()
        parser = Parser(tokens)
        expr = parser.expression()
        self.assertEqual(parser.parse_errors[0].message, "Expect ')' after expression.")
        self.assertEqual(parser.parse_errors[0].token.type, TokenType.EOF)



if __name__ == "__main__":
    unittest.main()
