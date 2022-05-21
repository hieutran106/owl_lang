from typing import Any
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
    expr_visitor: ExprVisitor

    def __init__(self, expr_visitor: ExprVisitor):
        self.expr_visitor = expr_visitor

    def visit_expression_stmt(self, stmt: ExpressionStmt) -> None:
        self.expr_visitor.evaluate(stmt.expression)

    def visit_print_stmt(self, stmt: PrintStmt) -> None:
        value = self.expr_visitor.evaluate(stmt.expression)
        print(stringify(value))

    def execute(self, stmt: Stmt):
        stmt.accept(self)
