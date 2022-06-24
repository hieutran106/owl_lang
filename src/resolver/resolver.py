from __future__ import annotations
from typing import List, Dict, TYPE_CHECKING, Union

import logging

from src.interpreter import Interpreter
from .expr_resolver import ExprResolver
from .stmt_resolver import StmtResolver
from src.parse_error import ResolverError

if TYPE_CHECKING:
    from src.owl_token import Token
    from src.owl_ast.expr import Variable, Assignment
    from src.owl_ast.stmt import Stmt

class Resolver:
    interpreter: Interpreter
    stmt_resolver: StmtResolver
    expr_resolver: ExprResolver
    resolver_errors: List[ResolverError]
    scopes: List[Dict[str, bool]]

    def __init__(self, interpreter: Interpreter):
        self.interpreter = interpreter
        self.resolver_errors = []
        self.scopes = []
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
        print(f"Declare {name}, scopes len = {len(self.scopes)}")

    def define(self, name: Token):
        if len(self.scopes) == 0:
            return
        inner_most = self.scopes[-1]
        inner_most[name.lexeme] = True

    def resolve_local(self, expr: Union[Assignment, Variable]):
        print(f"Start resolve local for {expr=}")
        name = expr.name
        size = len(self.scopes)
        # loop backward
        for index, scope in reversed(list(enumerate(self.scopes))):
            if name.lexeme in scope:
                depth = size - 1 - index
                # store depth between current scope and scope where the variable is defined
                self.interpreter.resolve(expr, depth)
                logging.info(f"{expr}:{depth=}")
                return

    def resolve(self, statements: List[Stmt]):
        try:
            self.stmt_resolver.resolve_statements(statements)
        except ResolverError as error:
            self.resolver_errors.append(error)