import unittest
from .test_utils import interpret_source


class TestClosure(unittest.TestCase):
    def test_closure_1(self):
        source = """
        fun makeCounter() {
            var i = 0;
            fun count() {
                i = i + 1;
                print i;
                return i;
            }
            return count;
        }
        
        var counter = makeCounter();
        var x = counter(); // "1".
        var y = counter(); // "2".
        """
        interpreter = interpret_source(source)
        self.assertEqual(interpreter.global_environment.values["x"], 1)
        self.assertEqual(interpreter.global_environment.values["y"], 2)