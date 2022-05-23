import unittest
from .test_utils import interpret_source


class TestBlockStmt(unittest.TestCase):

    def test_should_execute_block(self):
        source = """
        var a = "global a";
        {
            var a = "inner a";
            print a;
            {
                a = "change inner a";
            }
            print a;
        }
        print a;
        """
        interpreter = interpret_source(source)
        self.assertEqual(interpreter.curr_environment.values['a'], "global a");
