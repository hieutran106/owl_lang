import unittest
from .test_utils import interpret_source
import io
from contextlib import redirect_stdout

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

    def test_closure_2(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            source = """
            var a = "outer";
            {
              print a;
              a = "inner";
              print a;
            }
            """
            interpret_source(source)

        actual_std_out = buf.getvalue()
        expected_std_out = "outer\ninner\n"
        self.assertEqual(actual_std_out, expected_std_out)