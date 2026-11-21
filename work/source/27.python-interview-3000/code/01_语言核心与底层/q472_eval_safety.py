import ast

SAFE_OPS = {
    "add": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
}

def safe_calc(expr: str):
    """AST 白名单求值:只允许二元算术"""
    node = ast.parse(expr, mode="eval").body
    if not isinstance(node, ast.BinOp):
        raise ValueError("only binary operations allowed")
    op_name = {ast.Add: "add", ast.Sub: "sub", ast.Mult: "mul"}.get(type(node.op))
    if op_name is None:
        raise ValueError(f"operator {type(node.op).__name__} not allowed")
    a = ast.literal_eval(node.left)
    b = ast.literal_eval(node.right)
    return SAFE_OPS[op_name](a, b)

if __name__ == "__main__":
    print(safe_calc("2 + 3"))
    print(safe_calc("10 * 4"))
    for bad in ("__import__('os').system('ls')", "2 ** 8"):
        try:
            safe_calc(bad)
        except ValueError as e:
            print("blocked:", e)
