import ast

class MiniLint(ast.NodeVisitor):
    """找出过长的函数与裸 except"""
    def __init__(self, max_len=3):
        self.problems = []
        self.max_len = max_len
        self._fname = None

    def visit_FunctionDef(self, node):
        self._fname = node.name
        if len(node.body) > self.max_len:
            self.problems.append(
                f"line {node.lineno}: {node.name} has {len(node.body)} statements"
            )
        self.generic_visit(node)
        self._fname = None

    def visit_ExceptHandler(self, node):
        if node.type is None:
            self.problems.append(f"line {node.lineno}: bare except in {self._fname}")
        self.generic_visit(node)

SRC = """
def long_function():
    a = 1
    b = 2
    c = 3
    d = 4
    return a + b + c + d

def fragile():
    try:
        return int("x")
    except:
        return 0
"""

if __name__ == "__main__":
    checker = MiniLint(max_len=3)
    checker.visit(ast.parse(SRC))
    for p in checker.problems:
        print(p)
