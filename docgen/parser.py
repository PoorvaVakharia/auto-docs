import ast
from typing import List, Dict

def parse_python_file(file_path: str) -> List[Dict]:
    with open(file_path, "r") as f:
        tree = ast.parse(f.read())

    items = []

    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.FunctionDef):
            items.append({
                "type": "function",
                "name": node.name,
                "docstring": ast.get_docstring(node)
            })
        elif isinstance(node, ast.ClassDef):
            items.append({
                "type": "class",
                "name": node.name,
                "docstring": ast.get_docstring(node)
            })
    return items
