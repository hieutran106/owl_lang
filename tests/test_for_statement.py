import unittest
from .test_utils import interpret_source, parse_source
from src.interpreter import Interpreter
from src.resolver.resolver import Resolver

class TestForStatement(unittest.TestCase):

    def test_should_execute_for_loop(self):
        source = """
        var x = 0;
        for (var i = 5; i < 10; i=i+1) {
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

    def test_should_execute_for_loop_3(self):
        source = """
        for (var i = 5; i < 10; i=i+1) {
           print i;
        }
        """
        statements, _ = parse_source(source)

        interpreter = Interpreter()
        resolver = Resolver(interpreter)
        resolver.resolve(statements)
        # print(statements)
        x = interpreter.resolved_local_variables
        for key, value in x.items():
            print(f"\t {key} VALUE: {value}")



        source = """
                {
                    var i = 5;
                    while (i<10) {
                        {
                            print i;
                        }
                        i = i + 1;
                    }
                }
                """
        statements, _ = parse_source(source)
        interpreter = Interpreter()
        resolver = Resolver(interpreter)
        resolver.resolve(statements)
        # print(statements)
        x = interpreter.resolved_local_variables
        for key, value in x.items():
            print(f"\t {key} VALUE: {value}")



    def test_should_execute_for_loop_4(self):
        source = """
        {
            var i = 5;
            while (i<10) {
                {
                    print i;
                }
                i = i + 1;
            }
        }
        """
        interpreter = interpret_source(source)


if __name__ == "__main__":
    unittest.main()
