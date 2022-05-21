from typing import List

from .owl_ast.stmt import Stmt, PrintStmt, ExpressionStmt, VarDeclaration
from .owl_ast.expr import Expr, Literal, Grouping, Binary, Visitor, Unary, Variable, Assignment
from .token_type import TokenType
from .owl_token import Token


class ParseError(Exception):
    def __init__(self, token: Token, message: str):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
        self.token = token
        self.message = message

    def __str__(self):
        line = self.token.line
        lexeme = self.token.lexeme
        if self.token.type == TokenType.EOF:
            return f"[Line {line}] Error at end: {self.message}"
        else:
            return f"[Line {line}] Error at '{lexeme}': {self.message}"


class Parser:
    tokens: List[Token]
    current: int
    parse_errors: List[ParseError]

    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0
        self.parse_errors = []

    def parse(self) -> List[Stmt]:
        statements = []
        while not self.is_at_end():
            statements.append(self.declaration())
        return statements

    def declaration(self) -> Stmt:
        try:
            if self.match(TokenType.VAR):
                return self.variable_declaration()
            return self.statement()
        except ParseError as parse_error:
            self.parse_errors.append(parse_error)
            self.synchronize()
            return None

    def variable_declaration(self) -> Stmt:
        name = self.consume(TokenType.IDENTIFIER, "Expect variable name.")
        initializer: Expr = None
        if self.match(TokenType.EQUAL):
            initializer = self.expression()
        self.consume(TokenType.SEMICOLON, "Expect ';' after variable declaration.")
        return VarDeclaration(name, initializer)

    def statement(self) -> Stmt:
        if self.match(TokenType.PRINT):
            return self.print_statement()
        return self.expression_statement()

    def print_statement(self) -> Stmt:
        value = self.expression()
        self.consume(TokenType.SEMICOLON, "Expect ';' after value.")
        return PrintStmt(value)

    def expression_statement(self) -> Stmt:
        expr = self.expression()
        self.consume(TokenType.SEMICOLON, "Expect ';' after expression.")
        return ExpressionStmt(expr)

    def expression(self) -> Expr:
        return self.assignment()

    def assignment(self) -> Expr:
        expr = self.equality()
        if self.match(TokenType.EQUAL):
            equal_token = self.previous()
            value = self.assignment()
            if isinstance(expr, Variable):
                name: Token = expr.name
                return Assignment(name, value)

            self.error(equal_token, "Invalid assignment target.")
        return expr



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

        if self.match(TokenType.IDENTIFIER):
            name = self.previous()
            return Variable(name)

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
        error = ParseError(token, message)
        self.parse_errors.append(error)
        return error

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
