"""业务错误码注册表:域前缀加序号,集中登记并渲染(纯标准库)。"""

REGISTRY = {
    "USER_NOT_FOUND":       {"code": "U1001", "http": 404, "retryable": False},
    "USER_LOCKED":          {"code": "U1002", "http": 423, "retryable": False},
    "RATE_LIMITED":         {"code": "C2001", "http": 429, "retryable": True},
    "BALANCE_INSUFFICIENT": {"code": "P3001", "http": 422, "retryable": False},
    "UPSTREAM_TIMEOUT":     {"code": "S5001", "http": 504, "retryable": True},
}

codes = [m["code"] for m in REGISTRY.values()]
assert len(codes) == len(set(codes)), "错误码必须全局唯一"


def render(name, detail=None):
    meta = REGISTRY[name]
    body = {"code": meta["code"], "error": name, "retryable": meta["retryable"]}
    if detail:
        body["detail"] = detail
    return meta["http"], body


def catalog():
    """按域前缀分组,自动生成文档目录。"""
    grouped = {}
    for name, meta in REGISTRY.items():
        grouped.setdefault(meta["code"][0], []).append((meta["code"], name))
    return grouped


print(render("RATE_LIMITED", "60 秒后重试"))
for prefix, rows in sorted(catalog().items()):
    print(prefix, sorted(rows))
