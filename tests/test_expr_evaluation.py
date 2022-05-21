import unittest

from src.expr_visitor import ExprVisitor
from src.scanner import Scanner
from src.parser import Parser


def evaluate_source(source: str):
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()

    parser = Parser(tokens)
    expr = parser.expression()

    expr_visitor = ExprVisitor()
    return expr_visitor.evaluate(expr)


class TestExprEvaluation(unittest.TestCase):

    def test_plus_number(self):
        source = "3+4"
        value = evaluate_source(source)
        self.assertEqual(value, 7)

    def test_plus_string(self):
        source = '"Hello " + "World"'
        value = evaluate_source(source)
        self.assertEqual(value, "Hello World")

    def test_plus_string_number(self):
        source = '"Value:" + 3'
        value = evaluate_source(source)
        self.assertEqual(value, "Value:3.0")

    def test_complex_expr(self):
        source = '2*(3/-3)'
        value = evaluate_source(source)
        self.assertEqual(value, -2)

    def test_comparison(self):
        source = '"hello" == "hello"'
        value = evaluate_source(source)
        self.assertEqual(value, True)

        source = '"hello" != "hello1"'
        value = evaluate_source(source)
        self.assertEqual(value, True)


if __name__ == "__main__":
    unittest.main()
