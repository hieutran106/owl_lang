import unittest
from src.resolver.resolver import Resolver
from src.interpreter import Interpreter
from .test_utils import parse_source


class TestResolver(unittest.TestCase):
    def test_should_show_error_1(self):
        source = """
        var hieu = 100;
        {
            var a = 1;
            {
                {
                    {
                        var z = a + 1;
                    }
                }
            }
        }
        """
        statements, _ = parse_source(source)
        interpreter = Interpreter()
        resolver = Resolver(interpreter)
        resolver.resolve(statements)
        locals = interpreter.locals
        self.assertEqual(len(locals.items()), 1)
        first_key = list(locals.keys())[0]
        self.assertEqual(locals[first_key], 3)

    def test_should_show_error_2(self):
        source = """
        {
            var a = a + 1;
        }
        """
        statements, _ = parse_source(source)
        interpreter = Interpreter()
        resolver = Resolver(interpreter)
        resolver.resolve(statements)
        errors = resolver.resolver_errors
        self.assertEqual(errors[0].message, "Can't read local variable in its own initializer.")
