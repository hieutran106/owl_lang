from __future__ import annotations
from typing import List
from src.owl_ast.stmt import Stmt
from src.scanner import Scanner
from src.parser import Parser
from src.interpreter import Interpreter


def parse_source(source: str):
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()

    parser = Parser(tokens)
    statements = parser.parse()
    return statements, parser


def interpret_statements(statements: List[Stmt]):
    interpreter = Interpreter()
    interpreter.interpret(statements)
    return interpreter


def interpret_source(source: str):
    statements, _ = parse_source(source)
    return interpret_statements(statements)
