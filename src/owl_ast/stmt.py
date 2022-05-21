from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod
from .expr import Expr


class Stmt(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


@dataclass
class Expression(Stmt):
    expression: Expr
    
    def accept(self, visitor: Visitor):
        return visitor.visit_expression_expr(self)


@dataclass
class Print(Stmt):
    expression: Expr
    
    def accept(self, visitor: Visitor):
        return visitor.visit_print_expr(self)


class Visitor(ABC):
    
    @abstractmethod
    def visit_expression_expr(self, expr: Expression):
        pass
    
    @abstractmethod
    def visit_print_expr(self, expr: Print):
        pass
    