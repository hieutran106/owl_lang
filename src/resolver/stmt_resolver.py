from __future__ import annotations
from typing import TYPE_CHECKING, List

from owl_ast.stmt import FunctionDeclaration, VarDeclaration, WhileStmt, ReturnStmt, PrintStmt, IfStmt, ExpressionStmt, \
    BlockStmt, Stmt
from src.owl_ast.stmt import Visitor
if TYPE_CHECKING:
    from .resolver import Resolver
    from .expr_resolver import ExprResolver


class StmtResolver(Visitor):
    resolver: Resolver
    expr_resolver: ExprResolver

    def __init__(self, resolver: Resolver, expr_resolver: ExprResolver):
        self.resolver = resolver
        self.expr_resolver = expr_resolver

    def resolve_statements(self, statements: List[Stmt]):
        for stmt in statements:
            self.resolve_statement(stmt)

    def resolve_statement(self, statement: Stmt):
        statement.accept(self)

    def visit_block_stmt(self, stmt: BlockStmt) -> None:
        """
        This begins a new scope, traverses into block statements, and finally discard the scope
        """
        self.resolver.introduce_new_scope()
        self.resolve_statements(stmt.statements)
        self.resolver.end_scope()

    def visit_expression_stmt(self, stmt: ExpressionStmt) -> None:
        pass

    def visit_if_stmt(self, stmt: IfStmt) -> None:
        pass

    def visit_print_stmt(self, stmt: PrintStmt) -> None:
        pass

    def visit_return_stmt(self, stmt: ReturnStmt) -> None:
        pass

    def visit_while_stmt(self, stmt: WhileStmt) -> None:
        pass

    def visit_var_declaration(self, stmt: VarDeclaration) -> None:
        """
        Add a new entry to the innermost scope
        """
        self.resolver.declare(stmt.name)
        if stmt.initializer is not None:
            self.expr_resolver.resolve_expr(stmt.initializer)
        self.resolver.define(stmt.name)

    def visit_function_declaration(self, stmt: FunctionDeclaration) -> None:
        pass