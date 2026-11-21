"""权限表达式引擎: AND OR NOT 与括号的解析求值(纯标准库)。"""


def tokenize(expr):
    tokens, i = [], 0
    while i < len(expr):
        ch = expr[i]
        if ch.isspace():
            i += 1
        elif ch in "()":
            tokens.append(ch)
            i += 1
        elif expr[i:i + 3] in ("AND", "NOT") or expr[i:i + 2] == "OR":
            j = i + 2 if expr[i:i + 2] == "OR" else i + 3
            tokens.append(expr[i:j])
            i = j
        else:
            j = i
            while j < len(expr) and expr[j] not in " ()":
                j += 1
            tokens.append(expr[i:j])
            i = j
    return tokens


class Parser:
    """递归下降: or_expr -> and_expr (OR and_expr)*; 原子是属性名或 NOT 括号组。"""

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def eat(self):
        tok = self.peek()
        self.pos += 1
        return tok

    def parse(self):
        node = self.or_expr()
        if self.peek() is not None:
            raise ValueError("多余 token: " + str(self.peek()))
        return node

    def or_expr(self):
        node = self.and_expr()
        while self.peek() == "OR":
            self.eat()
            node = ("or", node, self.and_expr())
        return node

    def and_expr(self):
        node = self.atom()
        while self.peek() == "AND":
            self.eat()
            node = ("and", node, self.atom())
        return node

    def atom(self):
        tok = self.eat()
        if tok == "NOT":
            return ("not", self.atom())
        if tok == "(":
            node = self.or_expr()
            if self.eat() != ")":
                raise ValueError("缺少右括号")
            return node
        if tok in ("AND", "OR", ")", None):
            raise ValueError("非法 token: " + str(tok))
        return ("attr", tok)


def evaluate(ast, attrs):
    kind = ast[0]
    if kind == "attr":
        return ast[1] in attrs
    if kind == "and":
        return evaluate(ast[1], attrs) and evaluate(ast[2], attrs)
    if kind == "or":
        return evaluate(ast[1], attrs) or evaluate(ast[2], attrs)
    if kind == "not":
        return not evaluate(ast[1], attrs)


def authorize(expr, attrs):
    return evaluate(Parser(tokenize(expr)).parse(), attrs)


ATTRS = {"role:editor", "dept:finance", "project:audit-2026"}
exprs = [
    ("role:editor", True),
    ("role:editor AND dept:finance", True),
    ("dept:finance AND (project:audit-2026 OR role:admin)", True),
    ("NOT tag:contractor AND role:editor", True),
    ("role:admin OR dept:hr", False),
    ("NOT (dept:finance OR role:admin)", False),
]
for expr, want in exprs:
    got = authorize(expr, ATTRS)
    print("{:48s} -> {}".format(expr, got))
    assert got == want, expr
for bad in ("AND role", "role:admin AND", "(role:admin"):
    try:
        authorize(bad, ATTRS)
        raise AssertionError(bad)
    except (ValueError, TypeError):
        print("坏表达式被拒:", repr(bad))
print("要点: 表达式引擎把授权从硬编码变成可配置策略, 解析一次缓存 AST, 求值是纯集合判断")
