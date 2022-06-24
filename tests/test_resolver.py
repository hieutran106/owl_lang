import unittest
from src.resolver.resolver import Resolver
from src.interpreter import Interpreter
from .test_utils import parse_source
import io
from contextlib import redirect_stdout

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
        resolved_local_variables = interpreter.resolved_local_variables
        self.assertEqual(len(resolved_local_variables.items()), 1)
        first_key = list(resolved_local_variables.keys())[0]
        self.assertEqual(resolved_local_variables[first_key], 3)

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

    def test_should_show_error_3(self):
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
        self.assertEqual(len(errors), 1)

    def test_shoud_resolve_variable(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            source = """
            var x = "hello ";
            {
                var y = x ? "world" : "";
                {
                    var z = x + y;
                    print z;
                }
            }
            """
            statements, _ = parse_source(source)
            interpreter = Interpreter()
            resolver = Resolver(interpreter)
            resolver.resolve(statements)

            interpreter.interpret(statements)

        actual_std_out = buf.getvalue()
        expected_std_out = "hello world\n"
        self.assertEqual(actual_std_out, expected_std_out)
