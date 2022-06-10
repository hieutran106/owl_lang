from abc import ABC, abstractmethod
from typing import List


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
