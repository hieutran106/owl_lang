from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod
from .expr import Expr


class Stmt(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


@dataclass
class ExpressionStmt(Stmt):
    expression: Expr
    
    def accept(self, visitor: Visitor):
        return visitor.visit_expression_stmt(self)


@dataclass
class PrintStmt(Stmt):
    expression: Expr
    
    def accept(self, visitor: Visitor):
        return visitor.visit_print_stmt(self)


class Visitor(ABC):
    
    @abstractmethod
    def visit_expression_stmt(self, stmt: ExpressionStmt) -> None:
        pass
    
    @abstractmethod
    def visit_print_stmt(self, stmt: PrintStmt) -> None:
        pass
    