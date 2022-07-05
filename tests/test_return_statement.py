import unittest
from .test_utils import interpret_source


class TestReturnStatement(unittest.TestCase):
    def test_return_statement_1(self):
        source = """
        fun sum(a, b) {
            print a;
            return a + b;
        }
        var result = sum(1, 2);
        """
        interpreter = interpret_source(source)
        self.assertEqual(interpreter.global_environment.values["result"], 3)

    def test_return_statement_2(self):
        source = """
        fun fib(n) {
            if (n <=1) return 1;
            if (n == 2) return 2;
            return fib(n-2) + fib(n-1);
        }
        
        var result = fib(5);
        print result;
        """
        interpreter = interpret_source(source)
        self.assertEqual(interpreter.global_environment.values["result"], 8)