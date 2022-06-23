import unittest
from src.resolver.resolver import Resolver
from src.interpreter import Interpreter
from .test_utils import parse_source


class TestResolver(unittest.TestCase):
    def test_should_show_error_1(self):
        source = """
        fun bad() {
            var a = "first";
            var a = "second";
        }
        """
        statements, _ = parse_source(source)
        interpreter = Interpreter()
        resolver = Resolver(interpreter)


