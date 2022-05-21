from typing import List

from .owl_ast.stmt import Stmt
from .expr_visitor import ExprVisitor, Expr
from .stmt_visitor import StmtVisitor
from .parse_error import OwlRuntimeError
from rich import print
from .environment import Environment

class Interpreter:
    expr_visitor: ExprVisitor
    stmt_visitor: StmtVisitor
    runtime_errors: List[OwlRuntimeError]
    environment: Environment

    def __init__(self):
        self.environment = Environment()
        self.expr_visitor = ExprVisitor(self.environment)
        self.stmt_visitor = StmtVisitor(self.expr_visitor, self.environment)
        self.runtime_errors = []

    def interpret(self, statements: List[Stmt]):
        try:
            for stmt in statements:
                self.stmt_visitor.execute(stmt)
        except OwlRuntimeError as runtime_error:
            self.runtime_errors.append(runtime_error)
            print(runtime_error)
