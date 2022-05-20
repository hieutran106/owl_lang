from typing import List
from .error_message import OwlErrorMessage
from .owl_ast.expr import Expr, Literal, Grouping, Binary, Visitor, Unary
from .token_type import TokenType
from .owl_token import Token
from .parse_error import ParseError
from rich import print

class Parser:
    tokens: List[Token]
    current: int
    parse_errors: List[OwlErrorMessage]

    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0
        self.parse_errors = []

    def parse(self) -> Expr:
        try:
            expr = self.expression()
            return expr
        except ParseError as parse_error:
            return None

    def expression(self) -> Expr:
        return self.equality()

    def equality(self) -> Expr:
        expr = self.comparison()
        while self.match(TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL):
            operator = self.previous()
            right = self.comparison()
            expr = Binary(expr, operator, right)
        return expr

    def comparison(self) -> Expr:
        expr = self.term()
        while self.match(TokenType.GREATER, TokenType.GREATER_EQUAL, TokenType.LESS, TokenType.LESS_EQUAL):
            operator = self.previous()
            right = self.term()
            expr = Binary(expr, operator, right)
        return expr

    def term(self) -> Expr:
        expr = self.factor()
        while self.match(TokenType.MINUS, TokenType.PLUS):
            operator = self.previous()
            right = self.factor()
            expr = Binary(expr, operator, right)
        return expr

    def factor(self) -> Expr:
        expr = self.unary()
        while self.match(TokenType.SLASH, TokenType.STAR):
            operator = self.previous()
            right = self.unary()
            expr = Binary(expr, operator, right)
        return expr

    def unary(self) -> Expr:
        if self.match(TokenType.BANG, TokenType.MINUS):
            operator = self.previous()
            right = self.unary()
            return Unary(operator, right)
        return self.primary()

    def primary(self) -> Expr:
        if self.match(TokenType.FALSE):
            return Literal(value=False)
        if self.match(TokenType.TRUE):
            return Literal(value=True)
        if self.match(TokenType.NIL):
            return Literal(value=None)
        if self.match(TokenType.NUMBER, TokenType.STRING):
            token = self.previous()
            return Literal(value=token.literal)

        if self.match(TokenType.LEFT_PAREN):
            expr = self.expression()
            self.consume(TokenType.RIGHT_PAREN, "Expect ')' after expression.")
            return Grouping(expr)
        raise self.error(self.peek(), "Expect expression.")

    def consume(self, token_type: TokenType, message: str) -> Token:
        if self.check(token_type):
            return self.advance()
        raise self.error(self.peek(), message)

    def error(self, token: Token, message: str) -> ParseError:
        # OwlLang.error2(token, message)
        error_message = OwlErrorMessage(token, message)
        self.parse_errors.append(error_message)
        print(error_message)
        return ParseError(message)

    def synchronize(self):
        """
        Discard tokens until we reach the beginning of the next token
        :return:
        """
        self.advance()
        while not self.is_at_end():
            # end expression statement
            if self.previous().type == TokenType.SEMICOLON:
                return
            keywords = [
                TokenType.CLASS,
                TokenType.FUN,
                TokenType.VAR,
                TokenType.FOR,
                TokenType.IF,
                TokenType.WHILE,
                TokenType.PRINT,
                TokenType.RETURN
            ]
            if self.peek().type in keywords:
                return
            # otherwise advance
            self.advance()


    def match(self, *token_types: TokenType):
        for type in token_types:
            if self.check(type):
                self.advance()
                return True

        return False

    def check(self, type: TokenType) -> bool:
        if self.is_at_end():
            return False

        return self.peek().type == type

    def advance(self) -> Token:
        if not self.is_at_end():
            self.current += 1
        return self.previous()

    def is_at_end(self) -> bool:
        return self.tokens[self.current].type == TokenType.EOF

    def peek(self) -> Token:
        return self.tokens[self.current]

    def previous(self) -> Token:
        return self.tokens[self.current - 1]
