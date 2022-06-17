import unittest
from .test_utils import interpret_source

class TestTernary(unittest.TestCase):
    def test_ternary(self):
        source = """
        var x = 5 > 3 ? true : false;
        var y = 5 < 3 ? "True" : "False";
        """
        interpreter = interpret_source(source)
        self.assertEqual(interpreter.global_environment.values["x"], True)
        self.assertEqual(interpreter.global_environment.values["y"], "False")

    def test_nested_ternary(self):
        source = """
        var x = 5 > 3 ? (1 < 0 ? false : true) : (1 > 0 ? true : false);
        """
        interpreter = interpret_source(source)
        self.assertEqual(interpreter.global_environment.values["x"], True)