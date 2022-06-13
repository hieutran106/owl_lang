from __future__ import annotations
import unittest

from src.owl_ast.stmt import BlockStmt
from src.scanner import Scanner
from src.parser import Parser
from src.token_type import TokenType
from .test_utils import parse_source


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
        parser.parse()
        self.assertEqual(parser.parse_errors[0].message, "Expect expression.")
        self.assertEqual(parser.parse_errors[0].token.type, TokenType.EOF)

    def test_error_grouping(self):
        source = """
                (3+4
                """
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()
        parser = Parser(tokens)
        parser.parse()
        self.assertEqual(parser.parse_errors[0].message, "Expect ')' after expression.")
        self.assertEqual(parser.parse_errors[0].token.type, TokenType.EOF)

    def test_parse_block(self):
        source = """
        {
            var a = 1;
            var b = 2;
        }
        """
        statements, _ = parse_source(source)
        self.assertIsInstance(statements[0], BlockStmt)

    def test_parse_assignment(self):
        source = """
        var a = 0;
        a = 1 + 1;
        """
        statements, _ = parse_source(source)

    def test_parse_synchronize(self):
        source = """
        print "before";
        var a = 0
        for (var i=0; i < 10; i=i+1)
        """
        statements, parser = parse_source(source)
        self.assertEqual(len(parser.parse_errors), 2)


if __name__ == "__main__":
    unittest.main()
