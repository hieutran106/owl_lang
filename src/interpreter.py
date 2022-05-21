from typing import List

from .owl_ast.stmt import Stmt
from .expr_visitor import ExprVisitor, Expr
from .stmt_visitor import StmtVisitor
from .parse_error import OwlRuntimeError
from rich import print


class Interpreter:
    expr_visitor: ExprVisitor
    stmt_visitor: StmtVisitor
    runtime_errors: List[OwlRuntimeError]

    def __init__(self):
        self.expr_visitor = ExprVisitor()
        self.stmt_visitor = StmtVisitor(self.expr_visitor)
        self.runtime_errors = []

    def interpret(self, statements: List[Stmt]):
        try:
            for stmt in statements:
                self.stmt_visitor.execute(stmt)
        except RuntimeError as runtime_error:
            self.runtime_errors.append(runtime_error)
            print(runtime_error)
