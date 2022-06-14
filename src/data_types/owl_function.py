from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List



from environment import Environment
from owl_ast.stmt import FunctionDeclaration


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
        interpreter.stmt_visitor.execute_block(function_body, function_environment)

    def arity(self) -> int:
        return len(self.declaration.parameters)

    def __str__(self):
        return f"<fn {self.declaration.name.lexeme} >"
