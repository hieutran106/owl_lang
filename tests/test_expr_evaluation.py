import unittest
from src.scanner import Scanner
from src.parser import Parser
from src.interpreter import Interpreter


def interpret_source(source: str) -> Interpreter:
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()
    parser = Parser(tokens)
    expr = parser.parse()

    interpreter = Interpreter()
    interpreter.interpret(expr)
    return interpreter


class TestExprEvaluation(unittest.TestCase):

    def test_plus_number(self):
        source = "3+4"
        interpreter = interpret_source(source)
        self.assertEqual(len(interpreter.runtime_errors), 0)

    def test_plus_string(self):
        source = '"Hello " + "World"'
        interpreter = interpret_source(source)
        self.assertEqual(len(interpreter.runtime_errors), 0)

    def test_plus_string_number(self):
        source = '"Value:" + 3'
        interpreter = interpret_source(source)
        self.assertEqual(len(interpreter.runtime_errors), 0)


if __name__ == "__main__":
    unittest.main()
