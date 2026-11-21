"""受限表达式求值:AST 白名单遍历,结构级防御,杜绝属性链与函数调用。"""
import ast, operator

BIN_OPS = {ast.Add: operator.add, ast.Sub: operator.sub,
           ast.Mult: operator.mul, ast.Div: operator.truediv, ast.Pow: operator.pow}
UNARY_OPS = {ast.USub: operator.neg, ast.UAdd: operator.pos}


class UnsafeExpression(Exception):
    pass


def safe_eval(expr, variables=None, max_pow=10000):
    tree = ast.parse(expr, mode="eval")            # 拒绝多语句

    def visit(node):
        if isinstance(node, ast.Expression):
            return visit(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.Name):
            if variables and node.id in variables:
                return variables[node.id]
            raise UnsafeExpression(f"未知变量 {node.id}")
        if isinstance(node, ast.BinOp) and type(node.op) in BIN_OPS:
            left, right = visit(node.left), visit(node.right)
            if isinstance(node.op, ast.Pow) and abs(right) > 64:
                raise UnsafeExpression("幂指数过大")
            return BIN_OPS[type(node.op)](left, right)
        if isinstance(node, ast.UnaryOp) and type(node.op) in UNARY_OPS:
            return UNARY_OPS[type(node.op)](visit(node.operand))
        raise UnsafeExpression(f"不允许的语法 {type(node).__name__}")

    return visit(tree)


if __name__ == "__main__":
    print("合法:", safe_eval("(price - cost) * qty", {"price": 100, "cost": 60, "qty": 3}))
    assert safe_eval("2**10") == 1024
    attacks = [
        "__import__('os').system('ls')",
        "().__class__.__bases__",
        "(lambda: 1)()",
        "open('/etc/passwd')",
    ]
    for a in attacks:
        try:
            safe_eval(a)
            raise AssertionError("攻击样例不应通过")
        except (UnsafeExpression, SyntaxError) as e:
            print(f"拦截 {a[:32]!r:<36} -> {type(e).__name__}")
    print("AST 白名单沙箱通过")
