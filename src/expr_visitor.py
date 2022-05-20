from .owl_ast.expr import Unary, Literal, Grouping, Binary
from .owl_token import Token
from .token_type import TokenType
from .owl_ast.expr import Visitor, Expr
from .parse_error import OwlRuntimeError


class ExprVisitor(Visitor):
    def visit_binary_expr(self, expr: Binary):
        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)
        op_type = expr.operator.type
        if op_type == TokenType.MINUS:
            self.check_number_operands(left, right)
            return left - right
        elif op_type == TokenType.PLUS:
            # TODO - check type
            if isinstance(left, str) and isinstance(right, str):
                return left + right
            elif isinstance(left, float) and isinstance(right, float):
                return left + right
            elif isinstance(left, float) and isinstance(right, str):
                return str(left) + right
            elif isinstance(left, str) and isinstance(right, float):
                return left + str(right)
            else:
                raise OwlRuntimeError(expr.operator, "Cannot perform PLUS operator.")
        elif op_type == TokenType.SLASH:
            self.check_number_operands(left, right)
            return left / right
        elif op_type == TokenType.STAR:
            self.check_number_operands(left, right)
            return left * right
        elif op_type == TokenType.GREATER:
            self.check_number_operands(left, right)
            return left > right
        elif op_type == TokenType.GREATER_EQUAL:
            self.check_number_operands(left, right)
            return left >= right
        elif op_type == TokenType.LESS:
            self.check_number_operands(left, right)
            return left < right
        elif op_type == TokenType.LESS_EQUAL:
            self.check_number_operands(left, right)
            return left <= right
        elif op_type == TokenType.BANG_EQUAL:
            return not self.is_equal(left, right)
        elif op_type == TokenType.EQUAL_EQUAL:
            return self.is_equal(left, right)

        # unreachable
        return None

    def visit_grouping_expr(self, expr: Grouping):
        return self.evaluate(expr.expression)

    def visit_literal_expr(self, expr: Literal):
        return expr.value

    def visit_unary_expr(self, expr: Unary):
        right = self.evaluate(expr.right)
        op_type = expr.operator.type
        if op_type == TokenType.BANG:
            return not bool(right)
        elif op_type == TokenType.MINUS:
            self.check_number_operand(expr.operator, right)
            return -right
        # unreachable
        return None

    def evaluate(self, expr: Expr):
        return expr.accept(self)

    def is_equal(self, left, right):
        return left == right

    def check_number_operand(self, operator: Token, operand) -> None:
        if isinstance(operand, float):
            return
        raise OwlRuntimeError(operator, "Operand must be a number.")

    def check_number_operands(self, operator: Token, left, right) -> None:
        if isinstance(left, float) and isinstance(right, float):
            return
        raise OwlRuntimeError(operator, "Operands must be a numbers.")
