from typing import List, Any

from .owl_token import Token
from .owl_ast.stmt import Stmt
from .expr_visitor import ExprVisitor
from .stmt_visitor import StmtVisitor
from .parse_error import OwlRuntimeError
from rich import print
from .environment import Environment


class Interpreter:
    expr_visitor: ExprVisitor
    stmt_visitor: StmtVisitor
    runtime_errors: List[OwlRuntimeError]
    curr_environment: Environment

    def __init__(self):
        self.curr_environment = Environment()
        self.expr_visitor = ExprVisitor(self)
        self.stmt_visitor = StmtVisitor(self.expr_visitor, self)
        self.runtime_errors = []

    def interpret(self, statements: List[Stmt]):
        try:
            for stmt in statements:
                self.stmt_visitor.execute(stmt)
        except OwlRuntimeError as runtime_error:
            self.runtime_errors.append(runtime_error)
            print(runtime_error)

    def assign_variable(self, name: Token, value: Any):
        self.curr_environment.assign(name, value)

    def get_variable(self, name: Token):
        return self.curr_environment.get(name)

    def define_variable(self, name: str, value: Any):
        self.curr_environment.define(name, value)
