from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod
from .expr import Expr
from src.owl_token import Token
from typing import List


class Stmt(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


@dataclass
class BlockStmt(Stmt):
    statements: List[Stmt]
    
    def accept(self, visitor: Visitor):
        return visitor.visit_block_stmt(self)


@dataclass
class ExpressionStmt(Stmt):
    expression: Expr
    
    def accept(self, visitor: Visitor):
        return visitor.visit_expression_stmt(self)


@dataclass
class IfStmt(Stmt):
    condition: Expr
    then_branch: Stmt
    else_branch: Stmt
    
    def accept(self, visitor: Visitor):
        return visitor.visit_if_stmt(self)


@dataclass
class PrintStmt(Stmt):
    expression: Expr
    
    def accept(self, visitor: Visitor):
        return visitor.visit_print_stmt(self)


@dataclass
class VarDeclaration(Stmt):
    name: Token
    initializer: Expr
    
    def accept(self, visitor: Visitor):
        return visitor.visit_var_declaration(self)


class Visitor(ABC):
    
    @abstractmethod
    def visit_block_stmt(self, stmt: BlockStmt) -> None:
        pass
    
    @abstractmethod
    def visit_expression_stmt(self, stmt: ExpressionStmt) -> None:
        pass
    
    @abstractmethod
    def visit_if_stmt(self, stmt: IfStmt) -> None:
        pass
    
    @abstractmethod
    def visit_print_stmt(self, stmt: PrintStmt) -> None:
        pass
    
    @abstractmethod
    def visit_var_declaration(self, stmt: VarDeclaration) -> None:
        pass
    