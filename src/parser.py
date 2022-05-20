from typing import List
from .owl_ast.expr import Expr, Literal, Grouping, Binary, Visitor

from .owl_token import Token

class Parser:
    tokens: List[Token]
    current: int

    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0

    def expression(self) -> Expr:
        return self.equality()