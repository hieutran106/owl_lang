import unittest

from src.environment import Environment
from src.expr_visitor import ExprVisitor
from src.scanner import Scanner
from src.parser import Parser


def evaluate_source(source: str):
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()

    parser = Parser(tokens)
    expr = parser.expression()

    environment = Environment()
    expr_visitor = ExprVisitor(environment)
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

    def test_logical_or(self):
        source = 'true or false'
        value = evaluate_source(source)
        self.assertEqual(value, True)

        source = '"Hello" or false'
        value = evaluate_source(source)
        self.assertEqual(value, "Hello")

        source = '"" or 1'
        value = evaluate_source(source)
        self.assertEqual(value, 1)

        # return right value
        source = '"" or false'
        value = evaluate_source(source)
        self.assertEqual(value, False)

    def test_logical_and(self):
        source = 'true and false'
        value = evaluate_source(source)
        self.assertEqual(value, False)


if __name__ == "__main__":
    unittest.main()
