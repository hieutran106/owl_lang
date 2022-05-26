import unittest
from .test_utils import interpret_source


class TestWhileStatement(unittest.TestCase):

    def test_should_execute_body(self):
        source = """
        var x = 0;
        while (x<10) {
            x = x + 1;
        }
        """
        interpreter = interpret_source(source)
        self.assertEqual(interpreter.curr_environment.values['x'], 10)

    def test_should_skip_body(self):
        source = """
        var x = 0;
        while (false) {
            x = 1;
        }
        """
        interpreter = interpret_source(source)
        self.assertEqual(interpreter.curr_environment.values['x'], 0)