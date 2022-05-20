from dataclasses import dataclass
from typing import List, Tuple
import pathlib
from jinja2 import Environment, select_autoescape, FileSystemLoader

env = Environment(
    loader=FileSystemLoader(searchpath="./"), autoescape=select_autoescape()
)


@dataclass
class AstNode:
    class_name: str
    fields: List[Tuple[str, str]]


def define_ast(base_name: str, types: List[str]):
    ast_nodes = []
    for node_type in types:
        class_name = node_type.split(":")[0].strip()
        field_str = node_type.split(":")[1].strip()
        fields: List[Tuple[str, str]] = []
        for field in field_str.split(","):
            field_type, name = field.strip().split(" ")

            fields.append((field_type, name))

        node = AstNode(class_name, fields)
        ast_nodes.append(node)

    template = env.get_template("ast.template")
    ast_source = template.render(base_name=base_name, ast_nodes=ast_nodes)
    path_to = pathlib.Path("../owl_ast", f"{base_name.lower()}.py")
    path_to.write_text(ast_source, encoding="utf-8")
    # with open(f"{base_name.lower()}.py", "w") as file:
    #     file.write(ast_source)


if __name__ == "__main__":
    print("Generate owl_ast")
    define_ast("Expr", [
        "Binary   : Expr left, Token operator, Expr right",
        "Grouping : Expr expression",
        "Literal  : Any value",
        "Unary    : Token operator, Expr right"
    ])
