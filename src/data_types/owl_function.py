from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

from src.environment import Environment
from src.owl_ast.stmt import FunctionDeclaration


class OwlCallable(ABC):
    @abstractmethod
    def call(self, interpreter, arguments: List):
        pass

    @abstractmethod
    def arity(self) -> int:
        """
        Return number of function arguments
        """
        pass


@dataclass
class OwlFunction(OwlCallable):
    declaration: FunctionDeclaration

    def call(self, interpreter, arguments: List):
        function_environment = Environment(interpreter.global_environment)
        for (name, value) in zip(self.declaration.parameters, arguments):
            function_environment.define(name.lexeme, value)

        function_body = self.declaration.body
        try:
            interpreter.stmt_visitor.execute_block(function_body, function_environment)
        except OwlReturnValue as owl_return:
            return owl_return.value

    def arity(self) -> int:
        return len(self.declaration.parameters)

    def __str__(self):
        return f"<fn {self.declaration.name.lexeme} >"


class OwlReturnValue(Exception):
    def __init__(self, value):
        super().__init__()
        self.value = value
