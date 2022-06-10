import unittest
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