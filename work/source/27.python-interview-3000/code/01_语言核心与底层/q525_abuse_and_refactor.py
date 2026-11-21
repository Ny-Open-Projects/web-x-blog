def handler_abuse(**kwargs):               # 滥用:kwargs 黑洞,契约不可见
    return kwargs.get("user", {}).get("name", "?")

def handler_fixed(user_name: str = "?") -> str:
    return user_name                       # 重构:显式参数表达契约

def parse_with_try(s):
    """EAFP 正确用法:转换可能失败的类型"""
    try:
        return int(s)
    except ValueError:
        return 0

def collect_abuse(values):
    seen = []
    [seen.append(x * 2) for x in values]   # 滥用:推导式当循环用
    return seen

def collect_fixed(values):
    out = []
    for x in values:                       # 重构:普通 for 表达副作用
        out.append(x * 2)
    return out

if __name__ == "__main__":
    print(handler_abuse(user={"name": "Alice"}), handler_fixed("Alice"))
    print(parse_with_try("12"), parse_with_try("x"))
    print(collect_abuse([1, 2, 3]))
    print(collect_fixed([1, 2, 3]))
