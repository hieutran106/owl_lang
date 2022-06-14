import unittest
from .test_utils import interpret_source

class TestFunctionDeclaration(unittest.TestCase):
    def test_function_declaration_1(self):
        source = """
        fun sum(a, b) {
            var result = a + b;
            return result;
        }
        print sum;
        var result = sum(1, 2);
        """
        interpreter = interpret_source(source)
        print(1)