# -*- coding: UTF-8 -*-
import sys
from .scanner import Scanner
from .parser import Parser
from .interpreter import Interpreter
from rich import print


def runFile(interpreter: Interpreter):
    pass


def runPrompt(interpreter: Interpreter):
    print(f"The owl 🦉 programming language (v1.0.0)")
    print("Inspired by Bob Nystroms's lox and Python.")
    while True:
        line = input("> ")
        if len(line) == 0:
            break

        run(line, interpreter)


def run(source: str, interpreter: Interpreter):
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()
    # terminate if there are any scan errors
    if len(scanner.scan_errors) > 0:
        for error in scanner.scan_errors:
            print(error)
        return

    parser = Parser(tokens)
    expr = parser.parse()
    # terminate if there are any parse error
    if len(parser.parse_errors) > 0:
        for error in parser.parse_errors:
            print(error)
        return

    interpreter.interpret(expr)


if __name__ == "__main__":
    n = len(sys.argv) - 1
    interpreter = Interpreter()
    if n > 1:
        print("Usage: owl [script]")
    elif n == 1:
        runFile(sys.argv[1], interpreter)
    else:
        runPrompt(interpreter)
