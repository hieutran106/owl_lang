from __future__ import annotations
from typing import List, Dict, TYPE_CHECKING
from src.interpreter import Interpreter
from .expr_resolver import ExprResolver
from .stmt_resolver import StmtResolver
if TYPE_CHECKING:
    from src.owl_token import Token

class Resolver:
    interpreter: Interpreter
    stmt_resolver: StmtResolver
    expr_resolver: ExprResolver
    scopes: List[Dict[str, bool]]

    def __init__(self, interpreter: Interpreter):
        self.interpreter = interpreter
        self.expr_resolver = ExprResolver(self)
        self.stmt_resolver = StmtResolver(self, self.expr_resolver)

    def introduce_new_scope(self):
        empty_scope: Dict[str, bool] = {}
        self.scopes.append(empty_scope)

    def end_scope(self):
        self.scopes.pop()

    def declare(self, name: Token):
        # TODO - Why ?
        if len(self.scopes) == 0:
            return
        inner_most = self.scopes[-1]
        # Mark a name is 'not ready yet'
        inner_most[name.lexeme] = False

    def define(self, name: Token):
        if len(self.scopes) == 0:
            return
        inner_most = self.scopes[-1]
        inner_most[name.lexeme] = True

