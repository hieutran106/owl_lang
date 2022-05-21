from typing import List

from .expr_visitor import ExprVisitor, Expr
from .parse_error import OwlRuntimeError
from rich import print


class Interpreter:
    expr_visitor: ExprVisitor
    runtime_errors: List[OwlRuntimeError]

    def __init__(self):
        self.expr_visitor = ExprVisitor()
        self.runtime_errors = []

    def interpret(self, expr: Expr):
        try:
            value = self.expr_visitor.evaluate(expr)
            print(self.stringify(value))
        except OwlRuntimeError as runtime_error:
            self.runtime_errors.append(runtime_error)
            print(runtime_error)

    def stringify(self, object) -> str:
        if object is None:
            return "nil"
        text = str(object)
        if isinstance(object, float):
            if text.endswith(".0"):
                text = text[:-2]
        elif isinstance(object, bool):
            text = text.lower()

        return text
