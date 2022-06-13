import unittest
import unittest.mock
from .test_utils import interpret_source


class TestNativeFunctions(unittest.TestCase):
    def test_should_call_clock(self):
        source = """
        var x = clock();
        print x;
        """
        interpreter = interpret_source(source)
        self.assertIsNotNone(interpreter.curr_environment.values['x'])

    def test_should_call_number(self):
        source = """
        var x = "3.14";
        var y = number(x);
        """
        interpreter = interpret_source(source)
        self.assertEqual(interpreter.curr_environment.values['y'], 3.14)

    def test_should_call_input(self):
        source = """
        var x = input("Enter your name:");
        """
        input_value = "Hieu Tran"
        with unittest.mock.patch('builtins.input', return_value=input_value):
            interpreter = interpret_source(source)
            self.assertIsNotNone(interpreter.curr_environment.values['x'], input_value)

    def test_function_error1(self):
        source = """
        var x = 2;
        x();
        """
        interpreter = interpret_source(source)
        runtime_error = interpreter.runtime_errors[0]
        self.assertEqual(runtime_error.message, "Object is not callable.")
