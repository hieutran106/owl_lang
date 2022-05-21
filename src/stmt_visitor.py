from typing import Any

from .environment import Environment
from .owl_ast.stmt import VarDeclaration
from .expr_visitor import ExprVisitor
from .owl_ast.stmt import PrintStmt, ExpressionStmt, Visitor, Stmt


def stringify(value: Any) -> str:
    if value is None:
        return "nil"
    text = str(value)
    if isinstance(value, float):
        if text.endswith(".0"):
            text = text[:-2]
    elif isinstance(value, bool):
        text = text.lower()

    return text


class StmtVisitor(Visitor):
    environment: Environment
    expr_visitor: ExprVisitor

    def __init__(self, expr_visitor: ExprVisitor, environment: Environment):
        self.expr_visitor = expr_visitor
        self.environment = environment

    def visit_expression_stmt(self, stmt: ExpressionStmt) -> None:
        self.expr_visitor.evaluate(stmt.expression)

    def visit_print_stmt(self, stmt: PrintStmt) -> None:
        value = self.expr_visitor.evaluate(stmt.expression)
        print(stringify(value))

    def visit_var_declaration(self, stmt: VarDeclaration) -> None:
        init_value = None
        if stmt.initializer:
            init_value = self.expr_visitor.evaluate(stmt.initializer)
        # define variable in the environment
        self.environment.define(stmt.name.lexeme, init_value)

    def execute(self, stmt: Stmt):
        stmt.accept(self)
