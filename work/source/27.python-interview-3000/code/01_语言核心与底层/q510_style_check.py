import ast

MAX_LINE = 79

def check_source(source, filename="<demo>"):
    """最小风格检查器:行宽 + None 比较,演示「规则进工具」"""
    problems = []
    for i, line in enumerate(source.splitlines(), 1):
        if len(line) > MAX_LINE:
            problems.append(f"{filename}:{i}: line too long ({len(line)})")
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Compare):
            for comparator, op in zip(node.comparators, node.ops):
                if (isinstance(op, (ast.Eq, ast.NotEq))
                        and isinstance(comparator, ast.Constant)
                        and comparator.value is None):
                    problems.append(f"{filename}:{node.lineno}: use 'is' for None")
    return problems

SAMPLE = "x = None\nif x == None:\n    pass\nLONG = " + "y" * 90 + "\n"

if __name__ == "__main__":
    for p in check_source(SAMPLE):
        print(p)
