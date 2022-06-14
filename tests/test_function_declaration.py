import unittest
from .test_utils import interpret_source, parse_source

class TestFunctionDeclaration(unittest.TestCase):
    def test_function_declaration_1(self):
        source = """
        fun sum(a, b) {
            var result = a + b;
            print result;
        }
        sum(1, 2);
        """
        # statements, parser = parse_source(source)
        interpreter = interpret_source(source)

if __name__ == "__main__":
    unittest.main()