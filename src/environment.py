from typing import Dict, Any
from .parse_error import OwlRuntimeError
from .owl_token import Token


class Environment:
    values: Dict[str, Any]

    def __init__(self):
        self.values = {}

    def define(self, name: str, value: Any):
        # Bind a new name to a value, aka declaration + initialization
        self.values[name] = value

    def get(self, name: Token):
        if name.lexeme in self.values:
            return self.values[name.lexeme]
        raise OwlRuntimeError(name, f"Undefined variable '{name.lexeme}'.")
