import unittest
from .test_utils import interpret_source


class TestIfStatement(unittest.TestCase):

    def test_should_execute_then_branch(self):
        source = """
        var a = true;
        var b = 0;
        
        if (a)
            b = 1;
        else b = -1;
        """
        interpreter = interpret_source(source)
        self.assertEqual(interpreter.curr_environment.values['b'], 1)

    def test_should_execute_else_branch(self):
        source = """
        var a = false;
        var b = 0;

        if (a)
            b = 1;
        else b = -1;
        """
        interpreter = interpret_source(source)
        self.assertEqual(interpreter.curr_environment.values['b'], -1)

    def test_no_else_branch(self):
        source = """
        var a = false;
        var b = 0;

        if (a)
            b = 1;
        """
        interpreter = interpret_source(source)
        self.assertEqual(interpreter.curr_environment.values['b'], 0)
