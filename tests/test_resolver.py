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
                a = 2;
                {
                    a = 5;
                    {
                        var z = a + 1;
                        print z;
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
        print(locals)
        interpreter.interpret(statements)




