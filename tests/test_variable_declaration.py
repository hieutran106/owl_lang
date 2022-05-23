import unittest
from .test_utils import interpret_source, parse_source


class TestVariableDeclaration(unittest.TestCase):
    def test_should_declare_variable(self):
        source = """
        var a = 1;
        var b = 2;
        var c = a + b;
        """
        interpreter = interpret_source(source)
        env_values = interpreter.curr_environment.values
        self.assertEqual(env_values['a'], 1)
        self.assertEqual(env_values['b'], 2)
        self.assertEqual(env_values['c'], 3)

    def test_parse_var_decl_error(self):
        source = "var a = 1"
        _, parser = parse_source(source)
        error = parser.parse_errors[0]
        self.assertEqual(error.message, "Expect ';' after variable declaration.")

    def test_assignment_expression(self):
        source = """
        var a = 1;
        a = 2;
        """
        interpreter = interpret_source(source)
        env_values = interpreter.curr_environment.values
        self.assertEqual(env_values['a'], 2)

    def test_assignment_error(self):
        source = """
        a = 2;
        """
        interpreter = interpret_source(source)
        env_values = interpreter.curr_environment.values
        self.assertRaises(KeyError, lambda: env_values['a'])
        self.assertEqual(interpreter.runtime_errors[0].message, "Undefined variable 'a'.")
