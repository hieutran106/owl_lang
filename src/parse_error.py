from .token_type import TokenType


class OwlRuntimeError(Exception):
    def __init__(self, token, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
        self.token = token
        self.message = message

    def __str__(self):
        line = self.token.line
        lexeme = self.token.lexeme
        if self.token.type == TokenType.EOF:
            return f"[Line {line}] RuntimeError at end: {self.message}"
        else:
            return f"[Line {line}] RuntimeError at '{lexeme}': {self.message}"
