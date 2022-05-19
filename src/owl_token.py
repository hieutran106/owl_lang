from dataclasses import dataclass
from .token_type import TokenType
from typing import Any

@dataclass()
class Token:
    type: TokenType
    lexeme: str
    literal: Any
    line: int


if __name__ == "__main__":
    p = Token(TokenType.IF, "abc", 123, 13)
    print(p)
