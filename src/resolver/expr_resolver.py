from __future__ import annotations
from typing import TYPE_CHECKING
from owl_ast.expr import Variable, Unary, Literal, Grouping, FunctionCall, Binary, Logical, Ternary, Assignment, Expr
from src.owl_ast.expr import Visitor

if TYPE_CHECKING:
    from .resolver import Resolver


class ExprResolver(Visitor):
    resolver: Resolver

    def __init__(self, resolver: Resolver):
        self.resolver = resolver

    def resolve_expr(self, expr: Expr):
        expr.accept(self)

    def visit_assignment_expr(self, expr: Assignment):
        pass

    def visit_ternary_expr(self, expr: Ternary):
        pass

    def visit_logical_expr(self, expr: Logical):
        pass

    def visit_binary_expr(self, expr: Binary):
        pass

    def visit_functioncall_expr(self, expr: FunctionCall):
        pass

    def visit_grouping_expr(self, expr: Grouping):
        pass

    def visit_literal_expr(self, expr: Literal):
        pass

    def visit_unary_expr(self, expr: Unary):
        pass

    def visit_variable_expr(self, expr: Variable):
        pass
