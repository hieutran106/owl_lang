import unittest
from src.scanner import Scanner
from src.token_type import TokenType


class TestScanner(unittest.TestCase):

    def test_operators(self):
        source = "+-*/(){},.;"
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()
        self.assertEqual(len(tokens), len(source) + 1)

    def test_case2(self):
        source = """
        var x = 1;
        if (x >1) {
            x = 2;
        }
        """
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()
        last = tokens[-2]
        self.assertEqual(last.type, TokenType.RIGHT_BRACE)

    def test_case3(self):
        source = """
        5 > 3 ? true : false
        """
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()
        last = tokens[3]
        self.assertEqual(last.type, TokenType.QUESTION)

    def test_string_literal(self):
        source = """
        var x = "hello world"
        """
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()
        last = tokens[-2]
        self.assertEqual(last.type, TokenType.STRING)

    def test_operators_2(self):
        source = """
        >= <= != ==
        """
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()

        self.assertEqual(tokens[0].type, TokenType.GREATER_EQUAL)
        self.assertEqual(tokens[1].type, TokenType.LESS_EQUAL)
        self.assertEqual(tokens[2].type, TokenType.BANG_EQUAL)
        self.assertEqual(tokens[3].type, TokenType.EQUAL_EQUAL)

    def test_number_literal(self):
        source = """
        // this is a comment
        3.14
        // another comment
        """
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()
        self.assertEqual(tokens[0].type, TokenType.NUMBER)
        self.assertEqual(tokens[0].literal, 3.14)

    def test_keywords(self):
        source = """
        and or if else class print nil
        """
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()

        self.assertEqual(tokens[0].type, TokenType.AND)
        self.assertEqual(tokens[1].type, TokenType.OR)
        self.assertEqual(tokens[6].type, TokenType.NIL)


if __name__ == "__main__":
    unittest.main()
