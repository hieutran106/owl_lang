import unittest
from src.environment import Environment
from src.expr_visitor import ExprVisitor
from src.scanner import Scanner
from src.parser import Parser
from src.interpreter import Interpreter


def interprete_source(source: str):
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()

    parser = Parser(tokens)
    statements = parser.parse()

    interpreter = Interpreter()
    interpreter.interpret(statements)
    return interpreter


class TestVariableDeclaration(unittest.TestCase):
    def test_should_declare_variable(self):
        source = """
        var a = 1;
        var b = 2;
        var c = a + b;
        """
        interpreter = interprete_source(source)
        env_values = interpreter.environment.values
        self.assertEqual(env_values['a'], 1)
        self.assertEqual(env_values['b'], 2)
        self.assertEqual(env_values['c'], 3)

    def test_parse_var_decl_error(self):
        source = "var a = 1"
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()

        parser = Parser(tokens)
        parser.parse()
        error = parser.parse_errors[0]
        self.assertEqual(error.message, "Expect ';' after variable declaration.")
