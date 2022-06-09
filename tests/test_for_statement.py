import unittest
from .test_utils import interpret_source


class TestForStatement(unittest.TestCase):

    def test_should_execute_for_loop(self):
        source = """
        var x = 0;
        for (var i = 0; i < 10; i=i+1) {
            x = i;
        }
        """
        interpreter = interpret_source(source)
        self.assertEqual(interpreter.curr_environment.values['x'], 9)

    def test_should_execute_for_loop_1(self):
        source = """
        var x = 0;
        var i = 0;
        for (; i < 10; i=i+1) {
            x = i;
        }
        """
        interpreter = interpret_source(source)
        self.assertEqual(interpreter.curr_environment.values['x'], 9)

    def test_should_execute_for_loop_2(self):
        source = """
        var a = 0;
        var temp;
        // Print the first 21 elements in the Fibonacci sequence
        for (var b = 1; a < 10000; b = temp + b) {
          print a;
          temp = a;
          a = b;
        }
        """
        interpreter = interpret_source(source)
        self.assertEqual(interpreter.curr_environment.values['temp'], 6765)


if __name__ == "__main__":
    unittest.main()
